def max_candies(N, grid):
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = grid[0][0]
    
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    dp[1][0] = dp[0][0] + grid[1][0]
    
    for j in range(1, N):
        dp[1][j] = max(dp[1][j-1] + grid[1][j], dp[0][j] + grid[1][j])
    
    return dp[1][-1]