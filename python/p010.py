import sys
import math

# TODO: Extract into a helper file
def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

def solve(maxpn):
    return sum(pn for pn in range(2, maxpn) if isPrime(pn))

if __name__ == "__main__":
    print(solve(2_000_000))