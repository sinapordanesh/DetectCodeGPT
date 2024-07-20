def max_value_of_blocks(N, blocks):
    dp = [0] * (10**4 + 1)
    for w, s, v in blocks:
        for j in range(s, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)
    return max(dp)

# Sample Input 1
N = 3
blocks = [(2, 2, 20), (2, 1, 30), (3, 1, 40)]
print(max_value_of_blocks(N, blocks))

# Sample Input 2
N = 4
blocks = [(1, 2, 10), (3, 1, 10), (2, 4, 10), (1, 6, 10)]
print(max_value_of_blocks(N, blocks))

# Sample Input 3
N = 5
blocks = [(1, 10000, 1000000000)] * 5
print(max_value_of_blocks(N, blocks))

# Sample Input 4
N = 8
blocks = [(9, 5, 7), (6, 2, 7), (5, 7, 3), (7, 8, 8), (1, 9, 6), (3, 3, 3), (4, 1, 7), (4, 5, 5)]
print(max_value_of_blocks(N, blocks))