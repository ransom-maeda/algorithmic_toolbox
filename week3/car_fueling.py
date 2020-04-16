# python3
import sys

def compute_min_refills(distance, tank, stops):
    refills = 0
    current_position = 0
    idx = 0
    start_index = 0

    while(current_position + tank < distance):
        start_index = idx

        while(idx < len(stops) and stops[idx] - current_position <= tank):
            idx += 1
        
        if start_index == idx:
            return -1
        
        current_position = stops[idx - 1]
        refills += 1

    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
