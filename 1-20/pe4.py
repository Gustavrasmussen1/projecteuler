"""
Project Euler Problem 4 
Gustav Rasmussen
30-01-2016
"""
import timeit


def loop():

	for x in xrange(999*999,100*100,-1):

		if str(x) == ''.join(reversed(str(x))):

			for a in xrange(999,100,-1):
				for b in xrange(999,100,-1):
					if a*b == x:
						print x
						print a
						print b
						return 
						
					else:
						pass

		else:
			pass

loop()
# The answer is 906609
