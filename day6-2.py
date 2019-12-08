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
		orbs[y[1]].name = orbs[y[1]]
	return orbs

#count all orbits in file. returns int
def orbitcount(orbdict):
	c = 0
	for x in orbdict:
		c += orbdict[x].count()
	return c

def orbitmeet(orbdict,one,two):
	meetdict = {}
	#make a sub-dict for one to root path
	X = meetdict[one]
	while X.parent != None:
#		Null()
		meetdict.setdefault(X.name,X)
		X = X.parent

	#make a sub-dict for two to first shared node
	X = orbdict[two]
	while X.parent != None:
		if X in meetdict != true:
			meetdict.setdefault(X.name,X)
			X = X.parent
		else: break
	X = meetdict[X.name]
	while X.parent != None:
		meetdict.pop(X.name)
		X = X.parent
	meetdict.pop(X.name)
	return meetdict


#test section
orbitest = orbuild('day6-2test.txt')
print(orbitest)
orbitmeetest = orbitmeet(orbitest,'YOU','SAN')
print(orbitmeetest)
orbitestcount = orbitcount(orbitmeetest)
print(orbitestcount)
if orbitestcount != 4:
	print('orbitest failure')
	quit()
else: print('orbitest success')

loadfile = 'day6-1input.txt'
orbits = orbuild(loadfile)
print('The total orbits of %s are %i' % (loadfile,orbitcount(orbits)))
