import pylab

def average(f):
    return (lambda L: sum([f(x) for x in L])/len(L))

# use dict for data field
def generateGraph(dataPartition, func, xvals=None, title='Insert Title', xlabel='Insert x-label', ylabel='Insert y-label'):
    if not xvals:
        xvals = range(len(dataPartition))
    L = []
    for piece in dataPartition:
        L.append(func(piece))
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.bar(xvals, L, (xvals[1]-xvals[0])*0.8)
    pylab.show()

##def f(x):
##    return x*x
##
##generateGraph(L, average(f))
