""" 
Project Euler Problem 1 
Gustav Rasmussen
29-01-2016
"""

#Calculate the sum of all multiples of either 3 or 5 in the range of 0 to 1000

sum = 0

for i in range(0, 1000):
	if i % 3 == 0 or i % 5 == 0:
		sum += i
	else:
		pass

print sum
