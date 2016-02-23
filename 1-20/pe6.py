"""
Project Euler Problem 6 
Gustav Rasmussen
03-02-2016
"""
import time

start_time = time.clock()

n = 100

def sum_squares(n):

	summa = sum(map(lambda x: x**2, xrange(0,n+1,1)))
	return summa


def square_sum(n):

	square = (sum(xrange(0,n+1,1)))**2
	return square

print square_sum(n) - sum_squares(n)
# 25164150

print time.clock() - start_time, 'seconds'
# 0.000645158639167 seconds

# Another method

new_time = time.clock()

def problem6(r):
	return sum(r)**2 - sum(x**2 for x in r)

print problem6(xrange(0,100+1,1))

print time.clock() - new_time, 'seconds'
# slower than above method