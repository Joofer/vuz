M = int(input())
N = int(input())
A = []
MAT = []

for i in range(0, N):
    A.append(int(input()))
    
for i in range(0, M):
    MAT.append(A)
    
for i in range(0, M):
    print(MAT[i])
    
K = int(input()) - 1

for i in range(0, M):
    print(MAT[i][K])