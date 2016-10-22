import plotter
import datareader

data = datareader.parse('homelessdata.csv')

def category(row):
    try:
        return row['DOB'][-2]
    except:
        return 'X'

D = {str(x):[] for x in range(10)}
for row in data:
    if category(row) in '0123456789':
        D[category(row)].append(row)
M = []
for i in range(4,12):
    M.append(D[str(i%10)])
def f(row):
    return 100.0*row['Black']

plotter.generateGraph(M, plotter.average(f), xvals=list(range(1940,2020,10)), title='% Black by decade of birth', xlabel='decade', ylabel='percentage')

