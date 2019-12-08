#Solution for https://adventofcode.com/2019/day/6

import sys

class Orb(object):			#Orbit object that has a name and a single parent
	def __init__(self):
		self.name = None
		self.parent = None
	def count(self): 		#count all of the parents and grandparents this object has
#		iterate through all parents and increment by 1 for each until None
#		print('count method initiated')
		cnt = 0
		X = self
		while X.parent != None:
#			print(X.name)
#			print(X.parent)
			cnt +=1
			X = X.parent
#			print(cnt)
		return cnt

#build orbits from file function. returns dict
def orbuild(filename):
	file = open(filename,'r')
	#readline
	orbs = {}
	for x in file:
#		print(x)
		z = x.rstrip('\n')
		y = z.split(')')
#		print(y)
		orbs.setdefault(y[0],Orb())
		orbs.setdefault(y[1],Orb())
		orbs[y[1]].parent = orbs[y[0]]
		orbs[y[1]].name = y[1]
	return orbs

#count all orbits in file. returns int
def orbitcount(orbdict):
	c = 0
	for x in orbdict:
		c += orbdict[x].count()
	return c

#find the shortest route between two orbits, returns int
def orbitmeet(orbdict,one,two):
	meetdict = {}
	#make a sub-dict for one to root path
	X = orbdict[one]
	while X.name in orbdict:
#		Null()
		print('Adding %s' % X.name)
		meetdict.setdefault(X.name,X)
		X = X.parent
	print('After %s, meetdict is:' % one)
	print(meetdict)
	#make a sub-dict for two to first shared node
	X = orbdict[two]
	Y = Orb()
	while X.name in orbdict:
		if X.name not in meetdict:
			print('Adding %s' % X.name)
			meetdict.setdefault(X.name,X)
			X = X.parent
		else: break
	print('After %s, meetdict is:' % two)
	print(meetdict)

	Y = X.parent
	X.parent = None
	while Y.name in meetdict:
		print('Removing %s' % Y.name)
		meetdict.pop(Y.name)
		Y = Y.parent
	print("After cleanup, meetdict is:")
	print(meetdict)

	return len(meetdict)-3	#minus start, end, and one stop (counting jumps)


#test section
orbitest = orbuild('day6-2test.txt')
print(orbitest)
orbitestcount = orbitmeet(orbitest,'YOU','SAN')
print(orbitestcount)
if orbitestcount != 4:
	print('orbitest failure')
	quit()
else: print('orbitest success')

loadfile = 'day6-1input.txt'
orbits = orbuild(loadfile)
orbitmeetcount = orbitmeet(orbits,'YOU','SAN')
print('The shortest distance between YOU and SAN is %i jumps' % orbitmeetcount)
