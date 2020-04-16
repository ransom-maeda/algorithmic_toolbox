# Uses python3
import sys

def get_change(m):
    count = 0

    # Get dimes
    while(m >= 10):
        m=m-10
        count+=1
    
    # Get nickels
    while(m>=5):
        m=m-5
        count+=1
    
    # Remainder are pennies
    count+=m
    
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
