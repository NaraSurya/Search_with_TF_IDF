from base import Session, engine, Base
from models.corpus import Corpus
from function import resumeFunction as rf

# Base.metadata.create_all(engine)

# 3 - create a new session
# session = Session()

# test_corpus = Corpus('test','ini hanyalah test corpus','test corpus')

# session.add(test_corpus)
# session.commit()
# session.close()

# corpuses = session.query(Corpus).all()

# for corpus in corpuses : 
#     corpus.computeToken()
#     print(corpus.tokens)

print(rf.resume("test resume funtion logic laaa. logic logic logic logic logic logic logic"))
