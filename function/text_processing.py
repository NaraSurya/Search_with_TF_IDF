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
 
    text = text.rstrip()
    text= normalize_text(text)

    text_no_stopword = stopword.remove(text)
    text_stemmed =stemmer.stem(text_no_stopword)
   
    return text_stemmed

def tokenization(text) : 
    text = preTextProcessing(text)
    tokens = nltk.tokenize.word_tokenize(text)
    frequency = nltk.FreqDist(tokens)
    return dict(frequency.most_common())


stopword = createStopword(['saya','kamu', 'bukan','huruf','bagai'])
factory = StemmerFactory()
stemmer = factory.create_stemmer()