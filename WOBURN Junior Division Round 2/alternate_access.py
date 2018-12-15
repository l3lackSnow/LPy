A = int(input())
B = int(input())
U = int(input())
D = int(input())

dist = abs(A - B)
if A > B:
    joules = dist * D
elif B > A:
    joules = dist * U
    
print(joules)