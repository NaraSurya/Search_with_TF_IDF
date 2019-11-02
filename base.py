from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

DATABASE_URL="mysql+pymysql://root:@localhost:3306/db_corpus"
engine = create_engine(DATABASE_URL)
# connection = engine.connect()
# metadata = db.MetaData()
Session = sessionmaker(bind=engine)
Base = declarative_base()
