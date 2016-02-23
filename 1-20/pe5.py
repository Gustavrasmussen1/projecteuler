"""
Project Euler Problem 5 
Gustav Rasmussen
31-01-2016
"""
import time

start_time = time.clock()

def evenly_divisors(n):

	n_range = xrange(n,0,-1)
	evenly = False
	i = n 

	while not evenly:
		if all(i % n == 0 for n in n_range):
			print i
			evenly = True 
		else:
			i +=1

evenly_divisors(20)

print time.clock() - start_time, "seconds"
