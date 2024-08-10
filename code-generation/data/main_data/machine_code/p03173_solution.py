def min_total_cost(N, sizes):
    dp = [[0] * N for _ in range(N)]
    cumsum = [0] + list(itertools.accumulate(sizes))
    
    for l in range(1, N):
        for i in range(N-l):
            j = i + l
            dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i, j)) + cumsum[j+1] - cumsum[i]
    
    return dp[0][N-1]