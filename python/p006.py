def solve(n): 
    return pow(sum(range(1, n + 1)), 2) - sum(map(lambda x: x * x, range(1, n + 1)))

if __name__ == "__main__":
    print(solve(100))