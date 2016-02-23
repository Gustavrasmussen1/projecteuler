"""
Project Euler Problem 2 
Gustav Rasmussen
29-01-2016
"""

# Generating fibonacci numbers

def fib():
	# We start the sequence with 1 and 2 as described in the problem
	seq = [1,2]
	even_fibo = [2]
	new_fibo = 0

	while new_fibo <= 4000000: # The value of the new term does not exceed four million
		new_fibo = seq[-1] + seq[-2] # The next term is the sum of the previous two

		seq.append(new_fibo)

		if new_fibo % 2 == 0: # Collects the even fibonacci numbers in a seperate list
			even_fibo.append(new_fibo)
		else:
			pass

	print sum(even_fibo) # Calculates the sum of the even fibonacci numbers

fib()
# 4613732