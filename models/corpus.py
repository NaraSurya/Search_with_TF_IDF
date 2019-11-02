from sqlalchemy import Column, String, Integer, Date , Text

import sys
sys.path.insert(1, 'D:/Kuliah/semester 5/Sistem Temu Kembali Informasi/tugas/Search Document with TF-IDF/code')
from base import Base

class Corpus(Base):
    __tablename__ = 'tb_corpus'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
    resume = Column(Text)

    def __init__(self, title, body , resume):
        self.title = title
        self.body = body
        self.resume = resume















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

