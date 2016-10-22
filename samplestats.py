import datareader
data = []
def init():
    global data
    data = datareader.parse('homelessdata.csv')
def countOccurences(fieldName, value):
    count = 0
    for x in data:
        if x[fieldName] == value:
            count+=1
    return count
def countWithinRange(fieldName, lower, upper):
    
