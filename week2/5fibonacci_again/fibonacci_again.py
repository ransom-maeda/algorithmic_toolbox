# Uses python3
import sys

def pisano_period(m):
    first_num = 0
    second_num = 1
    for i in range(0, m * m):
        first_num, second_num = second_num, (first_num + second_num) % m

        if first_num == 0 and second_num == 1:
            return i + 1


def get_fibonacci_huge(n, m):
    pisano = pisano_period(m)
    n = n % pisano
    
    first_num = 0
    second_num = 1

    for i in range(n):
        first_num, second_num = second_num, (first_num + second_num)

    return (first_num % m)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
