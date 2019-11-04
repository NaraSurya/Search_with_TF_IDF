import math
import re 
import sys
sys.path.insert(1, 'D:/Kuliah/semester 5/Sistem Temu Kembali Informasi/tugas/Search Document with TF-IDF/code')
from base import Session
from models.corpus import Corpus
from function import text_processing as tp
from models.query import Query



def search(keywords):
    session = Session()
    corpuses = session.query(Corpus).all()
    for corpus in corpuses :
        corpus.computeToken()
    for corpus in corpuses : 
        print(corpus.tokens)
    keywords = tp.stopword.remove(keywords)
    keywords = keywords.split()
    querys = [Query(tp.normalize_text(keyword)) for keyword in keywords]
    total_corpus = len(corpuses)
    total_weight = {}
    

    for query in querys : 
        counter_df = 0
        print(query.keyword)
        for corpus in corpuses : 
            counter_df = counter_df+ corpus.isQueryExist(query.keyword)
            print("document : {} , TF : {} ".format(corpus.title , corpus.computeTF(query.keyword)))
        
        query.setDF(counter_df)
        print("df : {}".format(query.df))
        query.computeIDF(total_corpus)
        print("idf : {}".format(query.idf))
        print("idf+1 : {}".format(query.idf+1))
        for corpus in corpuses : 
            print("compute TF : {}".format(corpus.computeTF(query.keyword)))
            weight = corpus.computeTF(query.keyword)*(query.idf+1)
            print("wight {} : {}".format(corpus.title,weight))
            # print(weight)
            corpus.set_weight(query.keyword,weight)
            print("document : {} , weight : {}".format(corpus.title , corpus.get_weight(query.keyword)))
        print()
    
    print("total weight")

    for corpus in corpuses : 
        counter_weight = 0
        for query in querys : 
            counter_weight = counter_weight + corpus.get_weight(query.keyword)

        
        if(counter_weight != 0):
            total_weight[corpus] = counter_weight
        # print("document : {} , total weight : {}".format(corpus.title , total_weight[str(corpus.id)]))


    ranked = sorted(total_weight.items(), key = lambda x : x[1] , reverse=True)
    ranked = dict(ranked)
    print("document teratas")
    print(ranked)
    return corpuses, querys , ranked
