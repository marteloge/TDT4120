from sys import stdin

def qs(list):
	return [] if list==[]  else qs([x for x in list[1:] if x < list[0]]) + [list[0]] + qs([x for x in list[1:] if x >= list[0]]) 
	
def nedreGrense(A, nedre):
	min = 0
	max = len(A)-1
	mid = 0
	while min < max:
		if((min+max)/2)%2==1:
			mid = ((min+max)/2) + 1
		else:
			mid = (min+max)/2
		if A[mid]>=nedre:
			max = mid - 1
		else :
			min = mid + 1
	if A[min]>nedre and (min-1)>=0:
		min-=1
	return A[min]
	
def ovreGrense(A, ovre):
	min = 0
	max = len(A)-1
	mid = 0 
	while min<max:
		if((min+max)/2)%2==1:
			mid = ((min+max)/2) + 1
		else:
			mid = (min+max)/2
		
		if A[mid]<=ovre:
			min = mid+1
		else :
			max = mid-1
		
	if A[max]< ovre and max+1<=len(A)-1:
		max+=1
	return A[max]
	

liste = []
for x in stdin.readline().split():
	liste.append(int(x))

A = qs(liste)
for linje in stdin:

	ord = linje.split()
	minst = int(ord[0])
	maks = int(ord[1])
	min = None
	max = None
	if A[0]>=minst:
		min=A[0]
	if A[len(A)-1]<=maks:
		max=A[len(A)-1]
	if min == None:
		min = nedreGrense(A, minst)
	if max == None:
		max = ovreGrense(A, maks)
	print min, max
