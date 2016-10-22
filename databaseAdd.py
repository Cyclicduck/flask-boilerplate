from app import db
from spreadsheet import getRows
from models import Entry

def addRows(startRow, endRow):
    rows = getRows(startRow, endRow)
    for row in rows:
        db.session.add(Entry(row))
    db.session.commit()
def getAllRows():
    return db.session.query(Entry).all()
