from flask import request
import sys
sys.path.insert(1, 'D:/Kuliah/semester 5/Sistem Temu Kembali Informasi/tugas/Search Document with TF-IDF/code')
from function import resumeFunction as rf
from base import Session, engine, Base
from models.corpus import Corpus
from flask import render_template
from flask import redirect
def store(request):
    title = request.form.get("title")
    body = request.form.get("body")
    resume = rf.resume(body)

    Base.metadata.create_all(engine)
    session = Session()
    new_corpus = Corpus(title=title,body=body,resume=resume)

    session.add(new_corpus)
    session.commit()
    session.close()

    return redirect("http://127.0.0.1:5000/")
 

def show(id) : 
    session = Session()
    corpus = session.query(Corpus).filter(Corpus.id == id).scalar()
    corpus.body = "<br>".join(corpus.body.split("\n"))
    return render_template('show.html',corpus=corpus)

def edit(id) : 
    session = Session()
    corpus = session.query(Corpus).filter(Corpus.id == id).scalar()
    return render_template('create_corpus.html',corpus=corpus)

def update(id , request) : 
    session = Session()
    corpus = session.query(Corpus).get(id)
    corpus.title = request.form.get('title')
    if corpus.body != request.form.get('body'):
        corpus.body = request.form.get('body')
        resume = rf.resume(corpus.body)
    session.commit()
    corpus.body = "<br>".join(corpus.body.split("\n"))
    return render_template('show.html',corpus=corpus , update=1)

def delete(id):
    session = Session()
    corpus = session.query(Corpus).get(id)
    session.delete(corpus)
    session.commit()
    return redirect("http://127.0.0.1:5000/")


