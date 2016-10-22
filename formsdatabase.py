from spreadsheet import getRows, DATA_ROW_CONST, NUM_FIELDS
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from app import db

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Homeless(Base):
    __tablename__ = 'homeless'
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.String(8192))
    def __init__(self, row):
        s = ''
        k = len(row)
        for i in range(k-1):
            s += row[i]+'\x03'
        s += row[-1]
        self.response = s
    def getRow(self):
        return self.response.split('\x03')

##class Entry(Base):
##    __tablename__ = 'entrytable'
##
##    id = Column(Integer, primary_key=True)
##    name = Column(String(32))
##    timestamp = Column(String(32))
##    personID = Column(String(32))
##    phone = Column(String(16))
##    email = Column(String(32))
##    gender = Column(String(16))
##                      
##    fields = [Column(String(64)) for i in range(128)]
##    friendliness = [Column
##    def __init__(self, row):
##        self.timestamp = row[0]
##        self.name = row[1]
##        self.personID = row[2]
##        self.phone = row[3]
##        self.email = row[4]
##        self.gender = row[5]
##        self.friendliness = row[6]
        

class RowCounter(Base):
    __tablename__ = 'rowcounter'
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    
    def __init__(self, n):
        self.count = n
def addRows(startRow, endRow):
    rows = getRows(startRow, endRow)
    for row in rows:
        db.session.add(Homeless(row))
    db.session.commit()
def erase():
    try:
        for row in db.session.query(Homeless):
            db.session.delete(row)
        db.session.delete(db.session.query(RowCounter)[0])
        db.session.commit()
    except:
        return
def pullNewRows():
    try:
        x = db.session.query(RowCounter).all()[0]
    except:
        db.session.add(RowCounter(0))
        db.session.commit()
        pullNewRows()
        return
    nextRow = x.count+DATA_ROW_CONST
    try:
        row = getRows(nextRow, nextRow)[0]
        extra = NUM_FIELDS-len(row)
        for i in range(extra):
            row.append('')            
    except:
        return
    
    while (row[0] != ''):
        db.session.add(Homeless(row))
        nextRow += 1
        try:
            row = getRows(nextRow, nextRow)[0]
            extra = NUM_FIELDS-len(row)
            for i in range(extra):
                row.append('')  
        except:
            break
    db.session.delete(x)
    db.session.add(RowCounter(nextRow-DATA_ROW_CONST))
    db.session.commit()
def getAllRows():
    L = db.session.query(Homeless).all()
    return [x.getRow() for x in L]
