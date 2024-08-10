def max_happiness(N, T, dishes):
    dishes.sort(key=lambda x: x[0])
    dp = [[0] * (T + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for t in range(1, T + 1):
            dp[i][t] = dp[i - 1][t]
            if t >= dishes[i - 1][0]:
                dp[i][t] = max(dp[i][t], dp[i - 1][t - dishes[i - 1][0]] + dishes[i - 1][1])
    return dp[N][T]