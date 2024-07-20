def count_sequences(N, K):
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

    res = 0
    for k in range(K, N + 1):
        res = (res + dp[N][k] * dp[N - 1][N - k]) % MOD

    return res

N, K = map(int, input().split())
print(count_sequences(N, K))