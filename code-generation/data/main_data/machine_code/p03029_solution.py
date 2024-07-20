def maximum_apple_pies(A, P):
    return min(A * 3 + P, P // 2)

# Test cases
print(maximum_apple_pies(1, 3))
print(maximum_apple_pies(0, 1))
print(maximum_apple_pies(32, 21))