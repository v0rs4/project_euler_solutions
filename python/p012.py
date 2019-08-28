import math

def solve(maxdc):
    i = 1
    nn = 1
    while True:
        dc = 0
        j = 1
        while j < math.sqrt(nn):
            if nn % j == 0:
                if nn // j == j:
                    dc += 1
                else:
                    dc += 2
            j += 1
        if dc >= maxdc:
            return nn
        i += 1
        nn += i 


if __name__ == "__main__":
    print(solve(500))