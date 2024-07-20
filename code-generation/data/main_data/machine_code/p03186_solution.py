def max_tasty_cookies(A, B, C):
    total_cookies = 0
    if A > 0 and C > 0:
        total_cookies += min(A + 1, C)
        A -= min(A, C - 1)
        C -= min(A, C - 1)
    total_cookies += min(B, C)
    return total_cookies

# Test cases
print(max_tasty_cookies(3, 1, 4))
print(max_tasty_cookies(5, 2, 9))
print(max_tasty_cookies(8, 8, 1))