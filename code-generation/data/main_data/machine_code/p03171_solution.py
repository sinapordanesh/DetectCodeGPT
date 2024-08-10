def find_X_minus_Y(N, a):
    dp = [[0]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = a[i]
    
    for d in range(1, N):
        for i in range(N-d):
            if (N - d) % 2 == 1:
                dp[i][i+d] = max(a[i] - dp[i+1][i+d], a[i+d] - dp[i][i+d-1])
            else:
                dp[i][i+d] = max(dp[i][i+d-1] + a[i+d], dp[i+1][i+d] + a[i])
    
    return dp[0][-1]