N = int(input())
arr = []

while N > 0:
    arr.append(str(N%10))
    N = N // 10

print(arr)
