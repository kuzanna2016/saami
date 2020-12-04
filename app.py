from flask import Flask, request, render_template, Response
import mysql.connector
import re
import itertools
import networkx as nx

app = Flask(__name__)


def connect_to_db():
    global con
    global cur
    with open('config.txt', encoding='utf-8') as f:
        PASSWORD = f.read()
    con = mysql.connector.connect(host='127.0.0.1', port=3306, database='kuruch', user='root', password=PASSWORD)
    cur = con.cursor(dictionary=False)


def get_options_lists():
    global poses
    global from_sounds
    global to_sounds
    global text_columns
    global indexes_columns
    global values_columns

    cur.execute("""
    SELECT DISTINCT pos FROM kuruch.lexemes;
    """)
    res = cur.fetchall()
    poses = [r[0] for r in res if r[0] is not None]
    poses = sorted(poses, key=lambda x: x[1])
    cur.execute("""
    SELECT DISTINCT `from` FROM kuruch.alternations;
    """)
    res = cur.fetchall()
    from_sounds = [r[0] for r in res if r[0] is not None]
    from_sounds = sorted(from_sounds)
    cur.execute("""
        SELECT DISTINCT `to` FROM kuruch.alternations;
        """)
    res = cur.fetchall()
    to_sounds = [r[0] for r in res if r[0] is not None]
    to_sounds = sorted(to_sounds)

    text_columns = ['cyrillic', 'transcription', 'definition', 'def', 'form_cyrillic', 'form_transcription', 'grammar',
                    'root', 'form', 'meaning']
    values_columns = ['type', 'type_alternation', 'isCn', 'length', 'palatalization', 'voicing', 'isVowel']

    indexes_columns = {'pos':poses,'from':from_sounds,'to':to_sounds}
    create_graph()


def parse_filter(req):
    filter_dict = {}
    for s in req:
        name = s[0]
        table = name.split('.')[0].replace('filter_', '')
        column_value = name.split('.')[1]
        search = re.search(r'(\w*?)_(regex|\d\*?|)$', column_value)
        regex = None
        if search != None:
            column = search.group(1)
            if search.group(2) == 'regex':
                regex = s[1]
            else:
                value = search.group(2)
        else:
            column = column_value
            value = s[1]
        if value != '':
            if table not in filter_dict:
                filter_dict[table] = {}
            if column not in filter_dict[table]:
                filter_dict[table][column] = {'values': []}
            if regex:
                filter_dict[table][column]['regex'] = regex
            else:
                filter_dict[table][column]['values'].append(value)
    return filter_dict


def parse_show(req):
    show_dict = {}
    for s in req:
        name = s[0]
        table, column = name.split('.')
        if table not in show_dict:
            show_dict[table] = []
        show_dict[table].append(column)
    return show_dict


def parse_request(req):
    show_list = []
    filter_list = []
    for s in req.items():
        if s[0] == 'limit':
            limit = s[1]
            continue
        if 'filter' in s[0]:
            filter_list.append(s)
        else:
            show_list.append(s)
    show_dict = parse_show(show_list)
    filter_dict = parse_filter(filter_list)
    if limit == "no limit":
        limit = 1000;
    return limit, show_dict, filter_dict


def create_graph():
    global graph
    tables = ['lexemes', 'derivatives', 'suffixes', 'suffixes_forms', 'alternations', 'examples']
    db_dict = {'lexemes':{'examples':'id_lexeme',
                           'derivatives':'id_lexem'},
                'derivatives': {'lexemes':'id_lexem',
                                'examples':'id_lexem',
                                'alternations':'id_deriv',
                                'suffixes_forms':'id_suffix_form'},
                'alternations': {'suffixes_forms':'id_suffix_form',
                                 'derivatives':'id_deriv'},
                'suffixes_forms': {'suffixes':'id_suffix',
                                   'alternations':'id_suffix_form',
                                   'derivatives':'id_suffix_form'},
                'suffixes': {'suffixes_forms':'id_suffix'},
                'examples': {'derivatives':'id_lexem',
                             'lexemes':'id_lexem'}}
    graph = nx.Graph()
    graph.add_nodes_from(tables)
    for node, connections in db_dict.items():
        for connection, key in connections.items():
            graph.add_edge(node, connection, using=key)
    return graph


def search(filter_dict, show_dict, limit):
    conditions = []
    # selects = []
    for table, columns in filter_dict.items():
        for column, values in columns.items():
            conds = []
            if column in text_columns:
                if 'regex' in values:
                    regex = values['regex']
                    if regex == 'b':
                        conds = [f'({table}.`{column}` LIKE "{value}%")' for value in values['values']]
                    elif regex == 'e':
                        conds = [f'({table}.`{column}` LIKE "%{value}")' for value in values['values']]
                    elif regex == 'i':
                        conds = [f'({table}.`{column}` LIKE "%{value}%")' for value in values['values']]
                else:
                    conds = [f'({table}.`{column}` LIKE "%{value}%")' for value in values['values']]
            elif column in values_columns:
                if 'is' in column:
                    conds = [f'({table}.`{column}` = {value})' for value in values['values']]
                else:
                    conds = []
                    for value in values['values']:
                        if value == '0':
                            cond = f'({table}.`{column}` is NULL)'
                        else:
                            cond = f'({table}.`{column}` = "{value}")'
                        conds.append(cond)
            elif column in indexes_columns:
                conds = [f'({table}.`{column}` = "{indexes_columns[column][value]}")' for value in values['values']]
            conditions.extend(conds)
        select = ', '.join([f'{table}.`{column}`' for column in show_dict[table]])
        # selects.append(select)
    selects = []
    for table, columns in show_dict.items():
        for c in columns:
            selects.append(f'{table}.`{c}`')
    selects_str = ', '.join(selects)
    conditions = '\n AND '.join(conditions)

    tables = set(list(filter_dict.keys()) + list(show_dict.keys()))

    if len(tables) <= 1:
        joins = list(tables)[0]
    else:
        path = find_path(tables,graph)
        joins = put_inside_join(path, graph)

    if len(conditions) == 0:
        req = f"""
            SELECT {selects_str} FROM {joins}
            LIMIT {limit};
            """
    else:
        req = f"""
        SELECT {selects_str} FROM {joins}
        WHERE {conditions}
        LIMIT {limit};
        """
    print(req)
    cur.execute(req)
    res = cur.fetchall()
    return selects, res


def put_inside_join(path, graph, i=0):
    string = ''
    padding = '\t'*i
    if i+1 < len(path)-1:
        string = f'\n{padding}({path[i]} INNER JOIN ({put_inside_join(path, graph, i+1)})\n{padding}USING({graph.edges[path[i],path[i+1]]["using"]}))'
    else:
        string = f'\n{padding}({path[i]} INNER JOIN ({path[i+1]})\n{padding}USING({graph.edges[path[i],path[i+1]]["using"]}))'
    return string


def find_path(tables, graph):
    paths = []
    for x in itertools.combinations(tables,2):
        for path in nx.all_simple_paths(graph, *x):
            if all(table in path for table in tables):
                paths.append(path)
    return sorted(paths, key=lambda x: len(x))[0]


@app.route('/')
def index():
    global result, columns
    if request.args:
        limit, show_dict, filter_dict = parse_request(request.args)
        columns, result = search(filter_dict, show_dict, limit)

        return render_template('index.html', poses=enumerate(poses), from_sounds=enumerate(from_sounds), to_sounds=enumerate(to_sounds), columns=columns, result=result)
    return render_template('index.html', poses=enumerate(poses), from_sounds=enumerate(from_sounds), to_sounds=enumerate(to_sounds), columns=[], result=[])

@app.route("/getCSV")
def getPlotCSV():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    csv = ";".join(columns) + '\n' + '\n'.join([';'.join(r) for r in result])
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=data.csv"})

if __name__ == '__main__':
    connect_to_db()
    get_options_lists()
    app.run(debug=True)