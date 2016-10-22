rows = []
def init():
    global rows
    import formsdatabase
    #formsdatabase.pullNewRows()
    rows = formsdatabase.getAllRows()
def getCounts(rowNum):
    D = {}
    for row in rows:
        if row[rowNum] in D:
            D[row[rowNum]]+=1
        else:
            D[row[rowNum]] = 1
    return D
def getNumberList(rowNum):
    numList = []
    for row in rows:
        if row[rowNum] == '':
            continue
        try:
            numList.append(float(row[rowNum]))
        except:
            return None
    return numList
def average(numList):
    return sum(numList)/len(numList)
def stdev(numList):
    ans = 0.0
    mu = average(numList)
    for n in numList:
        ans += (n-mu)**2
    ans /= len(numList)
    return ans**0.5
def getAvg(rowNum):
    L = getNumberList(rowNum)
    if L:
        return average(L)
    return None
def getNumEntries(rowNum):
    L = getNumberList(rowNum)
    if L:
        return len(L)
    else:
        return 0
def getSD(rowNum):
    L = getNumberList(rowNum)
    if L:
        return stdev(L)
    return None
def getRating(row):
    L = [6,7,8,28,29,35,36]
    k = 0.0
    tot = 0.0
    for n in L:
        try:
            d = float(row[n])
            k += 1.0
            tot += d
        except:
            pass
    return tot/k
    
    
