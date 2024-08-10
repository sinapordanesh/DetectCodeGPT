def reordering_documents(n, m, documents):
    MOD = 10**9 + 7
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, i + 1):
            dp[i][j] = (dp[i - 1][j] * j + dp[i - 1][j - 1]) % MOD
    
    total_ways = 0
    for i in range(n // 2, n + 1):
        total_ways = (total_ways + dp[n][i]) % MOD
    
    return total_ways

# Sample Input
print(reordering_documents(6, 3, [1, 3, 4, 2, 6, 5])) # 4
print(reordering_documents(6, 6, [1, 3, 4, 2, 6, 5])) # 8
print(reordering_documents(4, 4, [4, 3, 1, 2])) # 0