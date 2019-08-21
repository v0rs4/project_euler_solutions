from math import sqrt, floor

def find_smallest_prime_factor(n):
    assert n >= 2

    for i in range(2, floor(sqrt(n))):
        if n % i == 0:
            return i
    
    return n

def solve(n):
    while True:
        p = find_smallest_prime_factor(n)

        if p < n:
            n //= p
        else:
            return n

if __name__ == "__main__" :
    # print(solve(600851475143))
    solve(600851475143)