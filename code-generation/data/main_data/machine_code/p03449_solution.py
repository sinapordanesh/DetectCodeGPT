def max_candies(N, candies):
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = candies[0][0]
    
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + candies[0][j]
    
    for j in range(N):
        dp[1][j] = dp[0][j] + candies[1][j]
    
    return dp[1][-1]