import sys
sys.path.insert(1, 'D:/Kuliah/semester 5/Sistem Temu Kembali Informasi/tugas/Search Document with TF-IDF/code')
from base import Session
from models.corpus import Corpus
from flask import render_template

def index(create_code=0):
    session = Session()
    corpuses = session.query(Corpus).order_by(Corpus.id.desc())
    return render_template('home.html', corpuses=corpuses)

def indexLSA(create_code=0):
    session = Session()
    corpuses = session.query(Corpus).order_by(Corpus.id.desc())
    return render_template('homeLSA.html', corpuses=corpuses)