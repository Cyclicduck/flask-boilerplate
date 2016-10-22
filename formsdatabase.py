from app import db
from spreadsheet import getRows, DATA_ROW_CONST, NUM_FIELDS
from models import Homeless, RowCounter

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
