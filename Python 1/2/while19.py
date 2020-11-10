N = int(input())
arr = []

while N > 0:
    arr.append(int(N%10))
    N = N // 10

print(arr)
