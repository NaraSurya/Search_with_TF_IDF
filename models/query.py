import math

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