def balls_and_boxes(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][1] = 1
    
    for i in range(1, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-j][j]) % MOD
    
    return dp[n][k]

# Sample Input
print(balls_and_boxes(4, 3))
print(balls_and_boxes(10, 3))
print(balls_and_boxes(100, 100))