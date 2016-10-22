def parse(filename):
    ''' Assumes the first line of the csv file
contains headers and the rest of the lines contain data. Parses ints and floats whenever possible.
'''
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    headers = lines[0].split(',')
    n = len(headers)
    ans = []
    for i in range(1,len(lines)):
        L = lines[i].split(',')
        D = {}
        for j in range(n):
            try:
                L[j] = int(L[j])
            except:
                try:
                    L[j] = float(L[j])
                except:
                    pass
            D[headers[j]] = L[j]
        ans.append(D)
    return ans
    
