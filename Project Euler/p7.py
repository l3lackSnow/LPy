# 10001st prime
# Question 7

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def primesUpTo(n = 10001):
    count = 0
    primes = [2]
    while count < n:
        for i in range(3, 99999999999999):
            prime = True
            for j in range(2, i):
                if i % j == 0 or j == 1:
                    prime = False
                    break
            else:
                if prime:
                    primes.append(i)
                    
                    count += 1
                    
    return primes[:-1]

print(primesUpTo())
                
