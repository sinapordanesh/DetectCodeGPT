def count_amidakuji(H, W, K):
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][1] = 1

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = (dp[i - 1][j - 1] * dp[i - 1][j] + dp[i - 1][j] * dp[i - 1][j + 1] * (j != W)) % 1000000007

    return dp[H][K]

H, W, K = map(int, input().split())
print(count_amidakuji(H, W, K))