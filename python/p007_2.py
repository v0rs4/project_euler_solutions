# Simple brutforce with a clever way of checking primality

from sys import maxsize
from itertools import islice
from math import sqrt, floor

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, floor(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    

def create_prime_gen():
    # return (x for x in range(1, maxsize) if all(x % y != 0 for y in range(2, x)))
    return (n for n in range(1, maxsize) if isPrime(n))

def solve(n):
    return next(islice(create_prime_gen(), n - 1, n))

if __name__ == "__main__":
    print(solve(10_001))