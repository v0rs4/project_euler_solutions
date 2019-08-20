def solve():
    res = 0
    a, b = 1, 1
    while b < 4_000_000:
        if b % 2 == 0:
            res += b
        a, b = b, a + b
    return res

if __name__ == "__main__":
	print(solve())