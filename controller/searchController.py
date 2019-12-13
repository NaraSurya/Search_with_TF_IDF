from flask import render_template
import sys
sys.path.insert(1, 'D:/Kuliah/semester 5/Sistem Temu Kembali Informasi/tugas/Search Document with TF-IDF/code/function')
import searchFunction as sf



def search(keyword):
    corpuses , querys , ranked = sf.search(keyword)
    return render_template('search.html', keyword=keyword , corpuses=corpuses, querys=querys , ranked=ranked)

def searchLSA(keyword):
    ranked = sf.searchUsingLSA(keyword)
    return render_template('searchLSA.html',ranked=ranked)