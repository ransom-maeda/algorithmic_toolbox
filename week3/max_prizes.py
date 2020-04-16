# Uses python3
import sys

def get_diff(remaining, next_value):
    return remaining - next_value
    

def optimal_summands(n):
    summands = []
    idx = 1

    while n > 0:
        initial_value = n
        n = get_diff(n, idx)

        if idx >= n:
            summands.append(initial_value)
            n = 0
        else:
            summands.append(idx)
        
        idx += 1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
