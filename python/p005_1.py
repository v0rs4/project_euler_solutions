# Bruteforce; gonna take a while to solve

def solve(n):
    i = 1
    while True:
        print(i)
        if all(i % j == 0 for j in range(1, n + 1)):
            return i
        i += 1
            

if __name__ == "__main__":
    print(solve(20))