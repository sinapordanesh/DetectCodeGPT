def frog_stones(N, C, heights):
    dp = [float('inf')] * N
    dp[0] = 0
    
    for i in range(1, N):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + (heights[i] - heights[j])**2 + C)
    
    return dp[-1]