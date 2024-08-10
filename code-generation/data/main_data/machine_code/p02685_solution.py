def num_ways_to_paint_blocks(N, M, K):
    MOD = 998244353
    dp = [[0] * (K + 2) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            dp[i][j] = (dp[i-1][j] * M) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1] * (M - 1)) % MOD
    return dp[N][K]

N, M, K = map(int, input().split())
print(num_ways_to_paint_blocks(N, M, K))