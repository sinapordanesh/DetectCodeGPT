def count_trees(N, D):
    mod = 998244353
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        dp[i] = dp[i-1] * D.count(i-1) % mod
    return dp[N]

# Sample Input
print(count_trees(4, [0, 1, 1, 2])) # Output: 2
print(count_trees(4, [1, 1, 1, 1])) # Output: 0
print(count_trees(7, [0, 3, 2, 1, 2, 2, 1])) # Output: 24