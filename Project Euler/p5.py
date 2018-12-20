# Smallest multiple
# Problem 5

# Kinda slow rn

"""

2520 is the smallest number that can be divided 
by each of the numbers from 1 to 10 without any 
remainder.

What is the smallest positive number that is 
evenly divisible by all of the numbers from 1 
to 20?

"""

factors = []
c = 0

for i in range(1, 21):
    #print("1")
    ii = i
    for j in range(1, 21):
        #print("3")
        while ii % j == 0 and i != 1 and j != 1:
            ii = ii / j
            #print("4")
            c += 1
        else:
            if factors.count(j) < c:
                for i in range(c-factors.count(j)):
                    factors.append(j)
                    #print("5")
            c = 0
            
factors.sort()
print(factors)

ans = 1
for i in factors:
    ans = ans * i
    
print(ans)
    
                