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
    count = 0
    for x in data:
        if type(x[fieldName]) == str:
            continue
        if x[fieldName] >= lower and x[fieldName] < upper:
            count += 1
    return count
def countEntered(fieldName):
    count = 0
    for x in data:
        if type(x[fieldName]) != str:
            count += 1
def average(fieldName):
    total = 0
    ctr = 0
    for x in data:
        if type(x[fieldName]) != str:
            total += x[fieldName]
            ctr += 1
    if ctr == 0:
        return 0
    return total/ctr
def stdev(fieldName):
    total = 0
    mean = average(fieldName)
    ctr = 0
    for x in data:
        if type(x[fieldName]) != str:
            total += (x[fieldName]-mean)**2
            ctr += 1
    if ctr == 0:
        return 0
    return (total/ctr)**0.5
def percentile(fieldName, pct):
    t = int(countEntered(fieldName)*pct/100)
    L = []
    for x in data:
        if type(x[fieldName]) != str:
            L.append(x[fieldName])
    L = sorted(L)
    return L[pct]

