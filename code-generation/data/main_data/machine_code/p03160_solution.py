def min_cost(N, heights):
    dp = [0] * N
    dp[1] = abs(heights[1] - heights[0])
    
    for i in range(2, N):
        dp[i] = min(dp[i-1] + abs(heights[i] - heights[i-1]), dp[i-2] + abs(heights[i] - heights[i-2]))
    
    return dp[-1]