import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker


Base = declarative_base()
engine = sa.create_engine('sqlite:///database.sqlite', connect_args={'check_same_thread':False})

def new_session():
    
    Session = sessionmaker()
    Session.configure(bind=engine)

    return Session()

sess = new_session()

class Data():
    created = sa.Column(sa.TIMESTAMP, server_default=sa.func.now(), onupdate=sa.func.current_timestamp())

class Song(Base, Data):
    __tablename__ = 'songs'
    id = sa.Column(sa.Integer, primary_key=True)
    artist = sa.Column(sa.String)
    title = sa.Column(sa.String)
    file = sa.Column(sa.String)
    playing = sa.Column(sa.Integer)

class Option(Base, Data):
    __tablename__ = 'options'
    key = sa.Column(sa.String, primary_key=True)
    value = sa.Column(sa.String)


def initialize_database():
    Base.metadata.create_all(engine)