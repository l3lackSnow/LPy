# Largest Palindrome Product
# Problem 4

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def larPal():
    pal = 0
    for i in range(1000, 900, -1):
        for j in range(1000, 900, -1):
            pal = i * j
            fir3 = str(pal)[:3]
           
            las3 = str(pal)[3:]

            if fir3 == las3[::-1]:
                return pal
            
print(larPal())
            
        
