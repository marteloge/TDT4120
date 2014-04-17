from sys import stdin, stderr

def FlydWarshall(nm, n):
    d=nm
    pred=[] # lage 2dim?
    for i in xrange(0,n):
        for j in xrange(0,n):
            d[i][j]=nm[i][j]
            pred[i][j]='NIL'

    for k in xrange(0,n):
        for i in xrange(0,n):
            for j in xrange(0,n):
                if d[i][k]*d[k][j]>d[i][j]:
                    d[i][j] = d[i][k]*d[k][j]
                    pred[i][j]=k
    return Path(0,n)


def Path(i,j):
    if pred[i][j]=='NIL':
        return i,j
    else:
        Path(i, pred[i][j])
        Path(pred[i][j], j)

def main():
    n = int(stdin.readline())
    sansynligheter = [float(x) for x in stdin.readline().split()]
    nabomatrise = []
    INF=100000

    for linje in stdin:
        naborad = [INF] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for i in xrange(0,n):
            naborad[i] = naboer[i]
        nabomatrise.append(naborad)
main()


