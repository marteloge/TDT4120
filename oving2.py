from sys import stdin
from collections import deque

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    nivaa= None
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0
	self.nivaa = 0
		

def dfs(rot):
    Q = [rot]
    while Q:
        temp = Q.pop()
        if temp.ratatosk:
            return temp.nivaa
        for n in temp.barn:
            Q.append(n)
            n.nivaa = (temp.nivaa + 1)
	
def bfs(rot):
    q = [rot]
    while q:
        temp = q.pop(0)
        if temp.ratatosk:
            return temp.nivaa
        for n in temp.barn:
            q.append(n)
            n.nivaa = (temp.nivaa + 1)

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print bfs(start_node)

