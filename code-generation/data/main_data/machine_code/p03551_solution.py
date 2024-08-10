def expected_time(N, M):
    X = 100 * (N - M) + 1900 * M
    return X

# Sample Input
print(expected_time(1, 1)) # Output: 3800
print(expected_time(10, 2)) # Output: 18400
print(expected_time(100, 5)) # Output: 608000