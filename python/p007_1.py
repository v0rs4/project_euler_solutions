# Simple inline brutforce

from sys import maxsize
from itertools import islice

def create_prime_gen():
    return (x for x in range(1, maxsize) if all(x % y != 0 for y in range(2, x)))

def solve(n):
    return next(islice(create_prime_gen(), n, n + 1))

if __name__ == "__main__":
    print(solve(10_001))