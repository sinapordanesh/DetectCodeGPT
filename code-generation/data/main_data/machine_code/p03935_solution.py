def max_sequence(n, m):
    mod = 998244353
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][1] = 1
    
    for j in range(1, m + 1):
        dp[1][j] = 1
    
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
    
    return dp[n][m]

print(max_sequence(4, 7))
print(max_sequence(12, 20))
print(max_sequence(16, 30))