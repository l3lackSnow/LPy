n, m, s = map(int, input().split())
b = list(map(int, input().split()))


t = 0

while s > 0:
    b.sort()
    t += 1
    s -= 1
    ref = b[0]
    

    if s < 1:
        for i in range(len(b)):
            if b[i] > 0:
                ref = b[i]
                break
            
    s += ref
    b.remove(ref)
    
    if s >= m:
        s = m
        
    if t >= n:
        break    
    
print(t)