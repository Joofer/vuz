N = int(input())
aN = []
k1 = -1
k2 = -1

for i in range(0, N):
    aN.append(int(input()))
    
for i in range(0, N):
    if k1 == -1:
        a1 = aN[i]
        k1 = i
    elif aN[i] < a1:
        a1 = aN[i]
        k1 = i
    if k2 == -1:
        if i != k1:
            a2 = aN[i]
            k2 = i
    elif aN[i] < a2 & i != k1:
        a2 = aN[i]
        k2 = i
        
print(a1, k1)
print(a2, k2)