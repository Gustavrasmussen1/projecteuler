"""
Project Euler Problem 3 
Gustav Rasmussen
30-01-2016
"""

n = 600851475143 
i = 2

while i < n ** 0.5:
    while n % i == 0:
        n = n / i
    i +=  1

print n