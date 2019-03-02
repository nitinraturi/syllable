from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import db_user,db_pass,db_host,db_name
# Creating an instance of declarative_base

Base = declarative_base()

class Syllables(Base):
    ''' This Class Contains all of the users '''
    __tablename__ = 'syllables'
    word = Column(String(80), nullable= False,primary_key= True)
    syllable = Column(String(80), nullable= False)


def get_engine():
    # return create_engine('sqlite:///sylable.db')
    return create_engine('mysql://{0}:{1}@{2}/{3}?charset=utf8'.format(db_user,db_pass,db_host,db_name))

def get_session():
    Base.metadata.bind = get_engine()
    DBSession = sessionmaker(bind=get_engine())
    session = DBSession()
    return session

if __name__ == "__main__":
    # Connecting to the database
    engine = get_engine()
    # Bind engine to Base
    Base.metadata.create_all(engine)
