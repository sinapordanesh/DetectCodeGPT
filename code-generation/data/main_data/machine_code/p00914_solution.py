def equal_sum_sets():
    while True:
        n, k, s = map(int, input().split())
        if n == 0 and k == 0 and s == 0:
            break
        dp = [[[0]*(s+1) for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                for l in range(1, s+1):
                    if l >= i:
                        dp[i][j][l] = dp[i-1][j-1][l-i] + dp[i-1][j][l]
                    else:
                        dp[i][j][l] = dp[i-1][j][l]
        print(dp[n][k][s])

equal_sum_sets()