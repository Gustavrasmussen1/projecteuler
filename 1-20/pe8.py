"""
Project Euler Problem 8
Gustav Rasmussen
23-02-2016
"""
import time
from operator import mul

start = time.time()

digit_file = open('pe8.txt', 'r').read() # 1000 digit number stored in pe8.txt

digit_list = map(int, str(digit_file))

n = 13
s = 13
highest_seq = []
highest_product = 0 


while n != 1000:
	current_seq = digit_list[n-s:n]

	if reduce(mul, current_seq) > highest_product:
		highest_product = reduce(mul, current_seq)
		highest_seq = current_seq
	else: 
		pass

	n += 1

print highest_seq
print highest_product

print time.time() - start, 'seconds'

# OUTPUT:
# [5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5]
# 23514624000
# 0.0320000648499 seconds