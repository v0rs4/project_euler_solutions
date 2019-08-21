import sys
from functools import reduce

def create_prime_gen():
    return (x for x in range(2, sys.maxsize) if all(x % y != 0 for y in range(2, x)))

def find_prime_factorization(n):
    pf = []
    pgen = create_prime_gen()
    while True:
        p = next(pgen)
        while n % p == 0:
            pf.append(p)
            n //= p
        if n == 1:
            return pf

def solve(n):
    return find_prime_factorization(n)
        

if __name__ == "__main__":
    # print(solve(600851475143))
    solve(600851475143)
