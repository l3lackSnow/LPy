# Sum Square Difference
# Problem 6

"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def sumSquares(n=100):
    squares = []
    for i in range(1, n+1):
        squares.append(i**2)
    return sum(squares)

def squareSum(n=100):
    squares = []
    for i in range(1, n+1):
        squares.append(i)
    res = sum(squares)
    return res ** 2

print(squareSum() - sumSquares())
