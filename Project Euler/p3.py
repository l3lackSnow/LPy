# Largest Prime Factor
# Problem 3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def largestPrime(n = 600851475143):
    factors = []
    for i in range(1, 600851475143+1):
        while n % i == 0 and i > 1:
            factors.append(i)
            n = n / i
            if n == 1:
              return factors
            
    factors = list(set(factors))
    factors.sort()
    return factors

largestPrime()
