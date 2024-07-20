def knapsack_problem(N, W, items):
    dp = [0] * (W + 1)
    
    for i in range(N):
        for j in range(W, items[i][1] - 1, -1):
            dp[j] = max(dp[j], dp[j - items[i][1]] + items[i][0])
    
    return dp[W]