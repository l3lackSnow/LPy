N = int(input())

nmasks = []
for i in range(N):
    nmasks.append(input())
    
M = int(input())
mmasks = []
for i in range(M):
    mmasks.append(input())
    
imp = 0

for mask in nmasks:
    if mask in mmasks:
        imp += 1
        
print(imp)