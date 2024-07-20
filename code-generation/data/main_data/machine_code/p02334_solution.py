def balls_and_boxes(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i < j:
                dp[i][j] = 0
            elif j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
    
    return dp[n][k] % MOD

# Sample Input
print(balls_and_boxes(5, 3))
print(balls_and_boxes(10, 5))
print(balls_and_boxes(100, 100))