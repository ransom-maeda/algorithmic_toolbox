#Uses python3

import sys

def largest_number(a):
    

    return "".join([str(i) for i in reversed(sorted(numbers))])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
