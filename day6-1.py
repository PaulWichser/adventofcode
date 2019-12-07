class Orb(object):			#Orbit object that has a name and a single parent
	def __init__(self):
		self.name = None
		self.parent = None
	def count(self): 		#count all of the parents and grandparents this object has
		#iterate through all parents and increment by 1 for each until None
		print('count method initiated')
		cnt = 0
#		X = self.parent
#		while X.parent.name != None:
#			cnt +1
#			X = X.parent
#			print(cnt)
		return cnt

#take input from command line for data text file
#read data text file to data
#build list of Orb objects from data
#if parent does not exist, create it before child (use index or count method)
#iterate through list and sum Orb.count
	#temporary Orb

A = Orb()
A.name = 'A'
B = Orb()
B.name = 'B'
B.parent = A
#print(B.name)
#print(B.parent.name)
#print(B.parent.parent)

D = Orb()
D.parent = B
D.name = 'D'
C = Orb()
C.parent = B
C.name = 'C'
orbits = [A,B,C,D]
#X = orbits[2]
#print(X.name)
C.count()
orbits[2].count()
Y = orbits[2].parent