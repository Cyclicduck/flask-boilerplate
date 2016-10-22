from spreadsheet import getRows
# php exec
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker()
DBSession.configure(bind=engine)
session = DBSession()
Base = declarative_base()
engine.create_all()
class Entry(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(Integer)

    def __init__(self, row):
        self.name = row[1]
        self.age = row[10]

def addRows(startRow, endRow):
    rows = getRows(startRow, endRow)
    for row in rows:
        e = Entry(row)
        session.add(e)
    session.commit()

def printRows():
    allRows = session.query(Entry).all()
    for row in allRows:
        print('Name: %s, Age: %s' % (row.name, row.age))
    
