import nltk
import re 
import string
import matplotlib.pyplot as plt
import math
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist




def createStopword(more_stopword = []) : 
    stop_factory = StopWordRemoverFactory().get_stop_words() 
    new_stop_word = stop_factory + more_stopword
    dictionary = ArrayDictionary(new_stop_word)
    stopword = StopWordRemover(dictionary)
    return stopword



def stemming(sentence) : 
    return stemmer.stem(sentence)

def normalize_text(text) : 
    text = text.lower()
    text = re.sub(r"\d+", " ", text)
    text = text.translate(str.maketrans("","",string.punctuation)).strip()
    return text

def preTextProcessing(text) : 
    global factory , stemmer , stopword
    full_text = ""
 
    for sentence in text :  
        sentence = normalize_text(sentence)
        full_text += sentence + "\n"

    full_text_no_stopword = stopword.remove(full_text)
    full_text_stemmed =stemmer.stem(full_text_no_stopword)
   
    return full_text_stemmed

def tokenization(text) : 
    text = preTextProcessing(text)
    tokens = nltk.tokenize.word_tokenize(text)
    frequency = nltk.FreqDist(tokens)
    return dict(frequency.most_common())




class Corpus : 

    def __init__ (self , corpus_file) : 
        # initialisasi
        self.corpus_file = corpus_file
        # read file and get text
        file =  open(self.corpus_file,"r")
        self.text = file.readlines()
        self.tokens = tokenization(self.text)
        self.weight = {}

    def computeTF(self,query) : 
        if query not in self.tokens: 
            return 0
        
        return self.tokens[query]
    
    def isQueryExist(self,query) : 
        if query not in self.tokens : 
            return 0
        return 1
    def addWeight(self,query,weight):
        self.weight[query] = weight

class Query:
    def __init__(self , keyword):
        self.keyword = keyword
        self.df = 0
        self.idf = 0
    
    def setDF(self , df):
        self.df = df
    def computeIDF(self , total_document):
        if self.df != 0 :
            self.idf = math.log10(total_document/self.df)
    
       



    
def search(keywords) : 
    files = ["corpus/habibie.txt" , "corpus/soekarno.txt", "corpus/hatta.txt"] 
    corpuses = [Corpus(file) for file in files]
    keywords = stopword.remove(keywords)
    keywords = keywords.split()
    print(keywords)
    querys = [Query(normalize_text(keyword)) for keyword in keywords]
    total_corpus = len(corpuses)
    total_weight = {}

    for query in querys : 
        counter_df = 0
        print(query.keyword)
        for corpus in corpuses : 
            counter_df = counter_df+ corpus.isQueryExist(query.keyword)
            print("document : {} , TF : {} ".format(corpus.corpus_file , corpus.computeTF(query.keyword)))
        
        query.setDF(counter_df)
        print("df : {}".format(query.df))
        query.computeIDF(total_corpus)
        print("idf : {}".format(query.idf))
        print("idf+1 : {}".format(query.idf+1))
        for corpus in corpuses : 
            weight = corpus.computeTF(query.keyword)*(query.idf+1)
            corpus.addWeight(query.keyword,weight)
            print("document : {} , weight : {}".format(corpus.corpus_file , corpus.weight[query.keyword]))
        print()
    
    print("total weight")
    for corpus in corpuses : 
        counter_weight = 0
        for query in querys : 
            counter_weight = counter_weight + corpus.weight[query.keyword]

        if(counter_weight != 0):
            total_weight[corpus.corpus_file] = counter_weight
        # print("document : {} , total weight : {}".format(corpus.corpus_file , total_weight[corpus.corpus_file]))


    ranked = sorted(total_weight.items(), key = lambda x : x[1] , reverse=True)
    ranked = dict(ranked)
    print("document teratas")
    print(ranked)
    return corpuses, querys , ranked

stopword = createStopword(['saya','kamu', 'bukan','huruf','bagai'])
factory = StemmerFactory()
stemmer = factory.create_stemmer()

      
        

