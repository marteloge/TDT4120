from sys import *
import traceback

def subgraftetthet(nabomatrise, startnode):
	n = len(nabomatrise)
	stack = [startnode]
	liste = [startnode]
	restnoder = []
	
	while(stack):
		temp = stack.pop()
		for kol in range(0,n):
			if nabomatrise[temp][kol]:
				if kol not in liste:
					stack.append(kol)
					liste.append(kol)
				
	for i in range(0,n):
		if i not in liste:
			restnoder.append(i)
			
			
	kanter = 0
	for i in restnoder:
		for j in range(0,n):
			if(nabomatrise[i][j] and j not in liste):
				kanter+=1
	
	if len(restnoder) == 0:
		return 0.0
	else:
		return float(kanter) / float(len(restnoder)**2)
	raise 1

def main():
    try:
        n = int(stdin.readline())
        nabomatrise = [None] * n # rader
        for i in range(0, n):
            nabomatrise[i] = [False] * n # kolonner
            linje = stdin.readline()
            for j in range(0, n):
                nabomatrise[i][j] = (linje[j] == '1')
        for linje in stdin:
            start = int(linje)
            print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
    except:
        traceback.print_exc(file=stderr)

main()
