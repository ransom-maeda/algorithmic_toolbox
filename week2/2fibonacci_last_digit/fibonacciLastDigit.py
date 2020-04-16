# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fib_list(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, (n + 1)):
        arr.append((arr[i - 1] + arr[i - 2]) % 10)
    return arr[n]

n = int(input())
#print(calc_fib(n))
print(fib_list(n))