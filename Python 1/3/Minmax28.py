N = int(input())
A = []
k = 0
c = 0
MAX = 0
for i in range(0, N):
    A.append(int(input()))
    
for i in range(0, N):
    if k == 0:
        n = i
        k = 1
        
    if A[i] != 0:
        c += 1
        k = 1
        
    elif c > MAX:
        MAX = c
        c = 0
        k = 0
    elif c <= MAX:
        c = 0
        k = 0

if c > MAX:
    MAX = c
        
if MAX != 0:
    print(n+1, MAX)
else:
    print(0, 0)