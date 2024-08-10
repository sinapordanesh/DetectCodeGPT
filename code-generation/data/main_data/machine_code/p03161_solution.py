def min_cost(N, K, heights):
    dp = [float('inf')] * N
    dp[0] = 0
    
    for i in range(1, N):
        for j in range(1, K+1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + abs(heights[i] - heights[i - j]))
    
    return dp[N-1]