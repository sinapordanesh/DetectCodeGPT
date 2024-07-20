def max_possible_sum(N, A):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
    return dp[N]

# Sample Input
print(max_possible_sum(6, [1, 2, 3, 4, 5, 6]))
print(max_possible_sum(5, [-1000, -100, -10, 0, 10]))
print(max_possible_sum(10, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]))
print(max_possible_sum(27, [18, -28, 18, 28, -45, 90, -45, 23, -53, 60, 28, -74, -71, 35, -26, -62, 49, -77, 57, 24, -70, -93, 69, -99, 59, 57, -49]))