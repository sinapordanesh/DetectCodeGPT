def three_way_branch(W, H, N, obstructions):
    MOD = 1000000009
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[1][1] = 1
    for x, y in obstructions:
        dp[y][x] = -1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if dp[i][j] == -1:
                continue
            if dp[i + 1][j - 1] != -1:
                dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD
            if dp[i + 1][j] != -1:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            if dp[i + 1][j + 1] != -1:
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
    return dp[H][W] % MOD

# Sample Input
print(three_way_branch(2, 4, 1, [(2, 1)]))
print(three_way_branch(2, 2, 1, [(2, 2)]))