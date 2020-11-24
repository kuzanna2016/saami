from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle
from scipy import sparse
from gensim.models import KeyedVectors
from search import search_tfidf, search_bm25, search_w2v_mean, search_w2v_matrices, find_answers
from preprocess_query import to_lemmas, to_stemms

app = Flask(__name__)

def initialize_all():
    global answers
    global questions
    global to_tf
    global tfidf_matrix
    global to_tfidf
    global bm25_matrix
    global w2v_matrices
    global w2v_matrix
    global w2v
    answers = pd.read_csv('data/final_answers.tsv',sep='\t',index_col=0)
    questions = pd.read_csv('data/final_questions.tsv', sep='\t')

    to_tfidf = pickle.load(open('vectorizers/to_tfidf', 'rb'))
    tfidf_matrix = sparse.load_npz('matrices/tfidf.npz')

    to_tf = pickle.load(open('vectorizers/to_tf', 'rb'))
    bm25_matrix = sparse.load_npz('matrices/bm25.npz')

    w2v_matrix = np.load('matrices/w2vmean.npy')
    w2v_matrices = np.load('matrices/w2vmatrices.npy', allow_pickle=True)

    w2v = KeyedVectors.load('word2vec/araneum_none_fasttextcbow_300_5_2018.model')


def search(query, search_method, top_n):
    if search_method == 'TF-IDF':
        query = to_stemms(query)
        search_result = search_tfidf(tfidf_matrix, query, to_tfidf, top_n=top_n)
    elif search_method == 'BM25':
        query = to_stemms(query)
        search_result = search_bm25(bm25_matrix, query, to_tf, top_n=top_n)
    elif search_method == 'word2vec_mean_vec':
        query = to_lemmas(query)
        search_result = search_w2v_mean(w2v_matrix, query, w2v, top_n=top_n)
    elif search_method == 'word2vec_matrix':
        query = to_lemmas(query)
        search_result = search_w2v_matrices(w2v_matrices, query, w2v, top_n=top_n)
    else:
        raise TypeError('unsupported search method')
    return find_answers(search_result, questions, answers)[::-1]


@app.route('/')
def index():
    if request.args:
        query = request.args['query']
        top_n = int(request.args['top_n'])
        search_method = request.args['search_method']
        answers = search(query, search_method, top_n)
        return render_template('index.html', answers=[(n+1,answer) for n,answer in enumerate(answers)], query=query)
    return render_template('index.html', answers=[], query='Your query')


if __name__ == '__main__':
    initialize_all()
    app.run(debug=True)