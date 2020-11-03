N = int(input())
A = []
B = []

for i in range(0, N):
    A.append(int(input()))
    
for i in range(0, N, 2):
    B.append(A[i])

print(B)

B = []
    
for i in range(1, N, 2):
    B.append(A[i])

print(B)