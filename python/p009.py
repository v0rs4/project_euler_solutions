def solve():
    for n in range(1, 1001):
        for m in range(n + 1, 1001):
            a, b, c = (m**2 - n**2, 2 * m * n, m**2 + n**2)
            if a + b + c == 1000:
                return a * b * c

if __name__ == "__main__":
    print(solve())