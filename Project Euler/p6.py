# Sum Square Difference
# Problem 6

"""

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
