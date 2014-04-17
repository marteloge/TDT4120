
from sys import stdin

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
    heap = []
    n=len(nm)
    done = [False]*n
    vektkant = [0]
    
    
    for i in xrange(0,n):
        if nm[0][i]<inf:
            heappush(heap,(nm[0][i], i))
    done[0]=true
    
    while(heap):
        vekt, node = heappop(heap)
        if not done[node]:
            if vekt > vektkant[0]:
                vektkant[0]=vekt
            if nm[node][i]<inf:
                for i in xrange(0,n)
                    heappush(heap,(nm[node][i],i))
        done[node]=true
        
    return vektkant[0]


def main()
    linjer = []
    for str in stdin:
        linjer.append(str)
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = [Inf] * n
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node][nabo] = vekt
        node += 1
    print mst(nabomatrise)
main()





    
