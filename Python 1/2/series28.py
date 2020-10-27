N = int(input("N: "))
A = []
K = N
for i in range(N):
    A.append(int(input()))

for i in range(N):
    A[i] = (A[i])**K
    K -= 1

print(A)
