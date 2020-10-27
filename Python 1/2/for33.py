N = int(input("N: "))
fib_arr = []

for i in range(0, N):
    if i == 0:
        fib_arr.append(int("1"))
    elif i == 1:
        fib_arr.append(int("1"))
    else:
        fib_arr.append(fib_arr[i-2] + fib_arr[i-1])

print(fib_arr)
