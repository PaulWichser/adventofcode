#Solution for https://adventofcode.com/2019/day/6

import sys

class Orb(object):			#Orbit object that has a name and a single parent
	def __init__(self):
		self.name = None
		self.parent = None
	def count(self): 		#count all of the parents and grandparents this object has
		#iterate through all parents and increment by 1 for each until None
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

#build orbits from file function
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
	return orbs
	#parse line with separator
	#check if parent exists, create if not
	#create child Orb

#count all orbits in file
def orbitcount(orbdict):
	c = 0
	for x in orbdict:
		c += orbdict[x].count()
	return c

#test section
orbitest = orbuild('day6-1test.txt')
orbitestcount = orbitcount(orbitest)
if orbitestcount != 42:
	print('orbitest failure')
	quit()
else: print('orbitest success')

loadfile = 'day6-1input.txt'
orbits = orbuild(loadfile)
print('The total orbits of %s are %i' % (loadfile,orbitcount(orbits)))
