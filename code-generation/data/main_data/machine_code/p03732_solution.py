def maximize_value(N, W, items):
    dp = [[0] * (W+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        for w in range(1, W+1):
            if items[i-1][0] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1][0]] + items[i-1][1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[N][W]