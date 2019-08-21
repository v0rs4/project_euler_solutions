def isPalindrome(n):
    return str(n) == str(n)[::-1]

def solve():
    return max(x * y for x in range(100, 1000) for y in range(100, 1000) if isPalindrome(x * y))

if __name__ == "__main__":
    print(solve())