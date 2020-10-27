N = int(input())
arr = []
arr_nech = []
K = 0

for i in range(N):
    arr.append(int(input()))
    if arr[i]%2 != 0:
        arr_nech.append(i)
        K += 1

print("Nech: ", arr_nech)
print("K: ", K)
