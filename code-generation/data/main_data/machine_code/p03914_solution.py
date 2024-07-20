def town_sequences(N, M):
    MOD = 1000000007
    
    dp = [[0] * N for _ in range(M + 1)]
    dp[0][0] = 1
    
    for i in range(1, M + 1):
        for j in range(N):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][(j + 1) % N]
            dp[i][j] %= MOD
    
    return dp[M][0] if N > 1 else 0

# Sample Input 1
print(town_sequences(3, 3))

# Sample Input 2
print(town_sequences(150, 300))

# Sample Input 3
print(town_sequences(300, 150))