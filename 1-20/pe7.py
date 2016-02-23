"""
Project Euler Problem 7 
Gustav Rasmussen
05-02-2016
"""

import time
from math import log, sqrt

start_time = time.clock()


prime_count = 1

x = 3
n = 10001

while prime_count != n:


	if all(x % i != 0 for i in xrange(2, x-1, 1)):
		prime_count += 1

		if prime_count == n:
			print x,'is the', prime_count,'th. prime number'
		else:
			x += 2
	else:
		x += 2
		
print time.clock() - start_time, 'seconds'

# Output:
# 104743 is the 10001 th. prime number
# 218.549974687 seconds - Waaaay too slow, I need to come back to this one.
