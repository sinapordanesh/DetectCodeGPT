def min_sum_wrongness(N, C, D, colors):
    dp = [[float('inf')] * C for _ in range(3)]
    for i in range(C):
        dp[i%3][i] = 0

    for i in range(3, N+1):
        for j in range(C):
            dp[i%3][j] = min(dp[(i-1)%3][k]+D[colors[i-1]-1][j] for k in range(C))

    return min(dp[N%3])