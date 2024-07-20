def discrete_speed(n, m, s, g, roads):
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for x, y, d, c in roads:
        dp[x][y] = dp[y][x] = d / c
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    if dp[s][g] == INF:
        return "unreachable"
    else:
        return "{:.5f}".format(dp[s][g])