def assign_scores(N, M):
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(i, N+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i][j-1] * i) % M
    return sum(dp[N]) % M

N, M = map(int, input().split())
print(assign_scores(N, M))