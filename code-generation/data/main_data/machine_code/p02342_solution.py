def balls_and_boxes(n, k):
    dp = [[0] * (n+1) for _ in range(k+1)]
    MOD = 10**9 + 7
    
    for i in range(1, k+1):
        for j in range(1, n+1):
            if i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1] * i) % MOD
    
    return dp[k][n]

n, k = map(int, input().split())
print(balls_and_boxes(n, k))