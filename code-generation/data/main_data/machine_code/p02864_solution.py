def min_operations(N, K, H):
    dp = [[float('inf')] * (N+1) for _ in range(N+1)]
    dp[0][0] = 0
    
    for i in range(1, N+1):
        for j in range(1, min(i, K)+1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], dp[k][j-1] + max(0, H[i-1] - H[k]))
    
    return dp[N][K]