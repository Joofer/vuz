N = int(input())
aN = []
k = 0
ktemp = 0

for i in range(0, N):
    aN.append(int(input()))
    
for i in range(0, N):
    for j in range(0, N):
        if aN[j] == aN[i]:
            ktemp += 1
    if ktemp > k:
        k = ktemp
    ktemp = 0
        
print(k)