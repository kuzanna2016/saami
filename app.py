from flask import Flask, request, render_template
import mysql.connector
import re

app = Flask(__name__)

def connect_to_db():
    global con
    global cur
    with open('config.txt', encoding='utf-8') as f:
        PASSWORD = f.read()
    con = mysql.connector.connect(host='127.0.0.1', port=3306, database='kuruch', user='root', password=PASSWORD)
    cur = con.cursor(dictionary=True)

def get_options_lists():
    global poses
    global from_sounds
    global to_sounds

    cur.execute("""
    SELECT DISTINCT pos FROM kuruch.lexemes;
    """)
    res = cur.fetchall()
    poses = [r['pos'] for r in res if r['pos'] is not None]
    poses = sorted(poses, key=lambda x: x[1])
    cur.execute("""
    SELECT DISTINCT `from` FROM kuruch.alternations;
    """)
    res = cur.fetchall()
    from_sounds = [r['from'] for r in res if r['from'] is not None]
    from_sounds = sorted(from_sounds)
    cur.execute("""
        SELECT DISTINCT `to` FROM kuruch.alternations;
        """)
    res = cur.fetchall()
    to_sounds = [r['to'] for r in res if r['to'] is not None]
    to_sounds = sorted(to_sounds)


def parse_filter(req):
    filter_dict = {}
    for s in req:
        name = s[0]
        table = name.split('.')[0].replace('filter_', '')
        if table not in filter_dict:
            filter_dict[table] = {}
        column_value = s[0].split('.')[1]
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


# def search(filter_dict, show_dict, limit):
#     for table, columns in filter_dict.items():
#         conditions = []
#         for column, values in columns.items():
#             if 'regex' in values:
#                 regex = values['regex']
#                 if regex == 'b':
#                     conds = [f'({table}.`{column}` LIKE "{value}%")' for value in values['values'] if len(value) > 0]
#                 elif regex == 'e':
#                     conds = [f'({table}.`{column}` LIKE "%{value}")' for value in values['values'] if len(value) > 0]
#                 elif regex == 'i':
#                     conds = [f'({table}.`{column}` LIKE "%{value}%")' for value in values['values'] if len(value) > 0]
#             else:
#                 conds = [f'({table}.`{column}` LIKE "%{value}%")' for value in values['values'] if len(value) > 0]
#             conditions.extend(conds)
#
#         selects = ', '.join([f'`{column}`' for column in show_dict[table]])
#         conditions = ' AND '.join(conditions)
#
#         req = f"""
#         SELECT {selects} FROM kuruch.{table}
#         WHERE {conditions}
#         LIMIT {limit};
#         """
#         print(req)
#         cur.execute(req)
#         res = cur.fetchall()
#         return show_dict[table], res
#         break


def search(table, filter_dict, show_dict, limit):
    columns = filter_dict[table]
    conditions = []
    for column, values in columns.items():
        if 'regex' in values:
            regex = values['regex']
            if regex == 'b':
                conds = [f'({table}.`{column}` LIKE "{value}%")' for value in values['values'] if len(value) > 0]
            elif regex == 'e':
                conds = [f'({table}.`{column}` LIKE "%{value}")' for value in values['values'] if len(value) > 0]
            elif regex == 'i':
                conds = [f'({table}.`{column}` LIKE "%{value}%")' for value in values['values'] if len(value) > 0]
        else:
            conds = [f'({table}.`{column}` LIKE "%{value}%")' for value in values['values'] if len(value) > 0]
        conditions.extend(conds)

    selects = ', '.join([f'`{column}`' for column in show_dict[table]])
    conditions = ' AND '.join(conditions)

    req = f"""
    SELECT {selects} FROM kuruch.{table}
    WHERE {conditions}
    LIMIT {limit};
    """
    print(req)
    cur.execute(req)
    res = cur.fetchall()
    return show_dict[table], res


@app.route('/')
def index():
    if request.args:
        print(request.args)
        limit, show_dict, filter_dict = parse_request(request.args)
        print(show_dict)
        print(filter_dict)
        columns, result = search('lexemes', filter_dict, show_dict, limit)
        # columns, result = search(filter_dict, show_dict, limit)
        print(columns)
        result = [list(r.values()) for r in result]
        print(result)
        return render_template('index.html', poses=enumerate(poses), from_sounds=enumerate(from_sounds), to_sounds=enumerate(to_sounds), columns=columns, result=result)
    return render_template('index.html', poses=enumerate(poses), from_sounds=enumerate(from_sounds), to_sounds=enumerate(to_sounds), columns=[], result=[])


if __name__ == '__main__':
    connect_to_db()
    get_options_lists()
    app.run(debug=True)