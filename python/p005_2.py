# Clever way by using lcm & gcd
# x * y = lcm(x,y) * gcd(x, y)
# lcm(x,y) == (x * y) / gcd(x, y)
# lcm(x,y,z) != (x * y * z) / gcd(x, y, z)
# lcm(x,y,z) == lcm(lcm(x,y), z)

from math import gcd
from functools import reduce

def solve(n):
    return reduce(lambda x, y: x * y // gcd(x, y), range(2, n + 1), 1)

if __name__ == "__main__":
    print(solve(20))