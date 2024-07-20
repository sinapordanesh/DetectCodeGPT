def count_ways(N, A, B, K):
    MOD = 998244353
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(K+1):
            dp[i][j] += dp[i-1][j] * (A+B) % MOD
            dp[i][j] %= MOD
            if j >= A:
                dp[i][j] += dp[i-1][j-A] * A % MOD
            dp[i][j] %= MOD
            if j >= A+B:
                dp[i][j] -= dp[i-1][j-A-B] * A % MOD
            dp[i][j] %= MOD

    return dp[N][K]