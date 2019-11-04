from sqlalchemy import Column, String, Integer, Date , Text

import sys
sys.path.insert(1, 'D:/Kuliah/semester 5/Sistem Temu Kembali Informasi/tugas/Search Document with TF-IDF/code')
from base import Base
import function.text_processing as tp

class Corpus(Base):
    __tablename__ = 'tb_corpus'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
    resume = Column(Text)
    # _weight = {}


    def __init__(self, title, body,resume):
        self.title = title
        self.body = body
        self.resume = resume
        self._weight = {}
    

    def computeToken(self):
        self.tokens = tp.tokenization(self.body)

    def computeTF(self,query) : 
        if query not in self.tokens: 
            return 0

        return self.tokens[query]

    def isQueryExist(self,query) : 
        if query not in self.tokens : 
            return 0
        return 1

    def set_weight(self,query,weight):
        if hasattr(self, '_weight'): 
            self._weight[query] = weight
           
        else : 
            self._weight = {}
            self._weight[query] = weight

    def get_weight(self,query):
        return self._weight[query]














# class Corpus : 

#     def __init__ (self) : 
#         self.table_corpus = dbConnection.db.Table('tb_corpus',dbConnection.metadata , autoload=True , autoload_with=dbConnection.engine)
#         self.column_keys = self.table_corpus.columns.keys()
#         query = db.select([self.table_corpus])
#         result_proxy = dbConnection.connection.execute(query)
#         result_set =result_proxy.fetchall()
#         self.data = result_set


# corpus = Corpus()
# print(corpus.data)

# def read():

