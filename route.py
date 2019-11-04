from flask import Flask
from flask import render_template
from flask import request
import sys
sys.path.insert(1, 'D:/Kuliah/semester 5/Sistem Temu Kembali Informasi/tugas/Search Document with TF-IDF/code')
from controller import searchController as sc
from controller import corpusController as cc
from controller import homeController as hc
app = Flask(__name__)

@app.route('/')
def home():
    return hc.index()

@app.route('/<name>')
def name(name):
    return render_template('test.html',name=name)

@app.route('/search')
def search():
    keyword = request.args.get('keyword', 'empty')
    return sc.search(keyword)

@app.route('/create-corpus')
def create_corpus(): 
    return render_template('create_corpus.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        return cc.store(request)
    return "error"

@app.route('/corpus/<id>')
def show(id):
    return cc.show(id)

@app.route('/corpus/edit/<id>')
def edit(id):
    return cc.edit(id)

@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        return cc.update(id,request)
    return "error"

@app.route('/corpus/delete/<id>')
def delete(id):
    return cc.delete(id)