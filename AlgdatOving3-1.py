

from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    toppnode=Node()
    for (ord, pos) in ordliste:
        temp = toppnode
        for n in ord:
            if not n in temp.barn:
                temp.barn[n] = Node()
            temp = temp.barn[n]
        
        temp.posi.append(pos)
    return toppnode

def posisjoner(ord, indeks, node): 

    if indeks >= len(ord):
        return node.posi
    elif ord[indeks] in node.barn:
        return posisjoner(ord, indeks+1, node.barn[ord[indeks]])
    elif ord[indeks] == '?':
	temp=[]
	for n in node.barn:
            temp.extend(posisjoner(ord, indeks+1, node.barn[ord[indeks]]))
	return temp
    else:
        return []

try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)







