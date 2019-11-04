import math
import re 
import sys
sys.path.insert(1, 'D:/Kuliah/semester 5/Sistem Temu Kembali Informasi/tugas/Search Document with TF-IDF/code')
from base import Session
from models.corpus import Corpus
from function import text_processing as tp
from models.query import Query

session = Session()

def resume(text):
    resume = ''
    weight_of_sentence = []
    corpuses = session.query(Corpus).all()
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s' , text)
    print(sentences)
    tokens = tp.tokenization(text)
    total_document = len(corpuses)
    # querys = [Query(tp.normalize_text(keyword)) for keyword in tokens.keys()]

    for sentence in sentences : 
        sentences_normalized = tp.normalize_text(sentence)
        sentence_no_stopword = tp.stopword.remove(sentences_normalized)
        sentence_stemmed = tp.stemming(sentence_no_stopword)
        words = sentence_stemmed.split(" ")
        counter = 0
        for word in words : 
            counter_df = 1
            for corpus in corpuses : 
                corpus.computeToken()
                counter_df = counter_df+ corpus.isQueryExist(word)
            
            print("word : {} , counter df : {}".format(word , counter_df))
            if word in tokens : 
                if counter_df != 0 and total_document != 0 :
                    counter = counter + tokens[word]*( math.log10(total_document/counter_df) + 1) 
                else : 
                    counter = counter + tokens[word]
        weight_of_sentence.append([sentence,counter])
        print(weight_of_sentence)

   
    ranked = sorted(weight_of_sentence,key=lambda x:x[1], reverse=True)
    print(ranked) 
    if len(ranked) >= 2 :
        for index in range (0,2) :
            resume = resume + ranked[index][0] 
    else : 
        return ranked[0][0]
    return resume