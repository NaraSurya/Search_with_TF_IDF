import math
import re 
import numpy as np
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
        print(corpus.title + ": \n")
        print(corpus.tokens)
        print("\n")
    keywords = tp.stopword.remove(keywords)
    keywords = tp.stemming(keywords)
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

def searchUsingLSA(keywords):
    # tokenisasi corpus
    session = Session()
    corpuses = session.query(Corpus).all()
    for corpus in corpuses :
        corpus.computeToken()
    for corpus in corpuses : 
        print(corpus.title + ": \n")
        print(corpus.tokens)
        print("\n")
    keywords = tp.stopword.remove(keywords)
    keywords = tp.stemming(keywords)
    keywords = keywords.split()
    querys = [Query(tp.normalize_text(keyword)) for keyword in keywords]
    # store the uniqe word
    uniqeWord =  []
    for corpus in corpuses : 
        for key in corpus.tokens.keys():
            uniqeWord.append(key)
    
    uniqeWord = unique(uniqeWord);
    print("Unique word : ")
    print(uniqeWord)
    print()

    corpus_title = []
    matriks = []
    queryMatriks = []
    for word in uniqeWord : 
        temp_matriks = []
        for corpus in corpuses :
            corpus_title.append(corpus.title) 
            if word in corpus.tokens :
                temp_matriks.append(corpus.tokens[word])
            else :
                temp_matriks.append(0)
        
        matriks.append(temp_matriks)
    
    for word in uniqeWord : 
        if word in keywords : 
            queryMatriks.append(1)
        else : 
            queryMatriks.append(0)

    print("Bag of WOrd : ")
    print(matriks)
    print()

    u,s,v = np.linalg.svd(matriks)
    v = transpose(v)
    print("matriks U : ")
    print(u)
    print()

    print("matriks S : ")
    print(s)
    print()

    print("matriks V : ")
    print(v)
    print()

    uk = get2Column(u)
    vk = get2Column(v)
    sk = get2row2column(s)

    print("Matriks uk : ")
    print(uk)
    print()

    print("Matriks sk : ")
    print(sk)
    print()

    print("Matriks vk : ")
    print(vk)
    print()

    qxuk = perkalian(queryMatriks , uk)
    rank2q = perkalian(qxuk,sk)

    print("Matirks rank2q : ")
    print(rank2q)
    print()

    similarity = {}

    for i in range(len(corpuses)) : 
        nom = (rank2q[0] * vk[i][0]) + (rank2q[1]*vk[i][1])
        denom = math.sqrt(rank2q[0]**2 + rank2q[1]**2) * math.sqrt(vk[i][0]**2 + vk[i][1]**2)
        similarity[corpuses[i]] = nom / denom

    print(similarity)
    ranked = sorted(similarity.items(), key = lambda x : x[1] , reverse=True)
    ranked = dict(ranked)
    print("document teratas")
    print(ranked)

    return ranked

def unique(words):
    unique_list = []
    for word in words : 
        if word not in unique_list : 
            unique_list.append(word)
    
    return unique_list


def get2Column(matriks):
    newMatriks = []
    for matrik in matriks : 
        newMatriks.append(matrik[:2])
    return newMatriks

def get2row2column(matriks):
    newMatriks = []
    newMatriks.append([1/matriks[0],0])
    newMatriks.append([0,1/matriks[1]])
    return newMatriks

def transpose(matriks):
    rez = [[matriks[j][i] for j in range(len(matriks))] for i in range(len(matriks[0]))]
    return rez

def perkalian(X,Y):
    result = []
    for i in range(len(Y[0])):
        temp = 0
        for j in range(len(X)) : 
            temp = temp + X[j]*Y[j][i]
        result.append(temp)
    
    return result
 


