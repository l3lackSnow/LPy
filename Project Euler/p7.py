# 10001st prime
# Problem 7

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def nthPrime(n = 10001):
    import math
    sieve = {}
    primes = []
    count = 0
    for i in range(2, 1000000+1):
        sieve[i] = True
        
    for i in range(2, int(math.sqrt(1000000))):
        for j in range(i, 1000000+1, i):
            if j == i:
                pass
            else:
                sieve[j] = False
                
    for k, v in sieve.items():
        if sieve[k]:
            primes.append(k)
            count += 1
            if count > n:
                return primes[-2:-1]
            
            
print(nthPrime())
