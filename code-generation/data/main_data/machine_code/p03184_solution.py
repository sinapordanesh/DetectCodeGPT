def count_paths(H, W, N, wall_squares):
    MOD = 10**9 + 7
    
    dp = [[0] * (W+1) for _ in range(H+1)]
    dp[1][1] = 1
    
    for r, c in wall_squares:
        dp[r][c] = -1
    
    for i in range(1, H+1):
        for j in range(1, W+1):
            if dp[i][j] != -1:
                if dp[i-1][j] != -1:
                    dp[i][j] += dp[i-1][j]
                if dp[i][j-1] != -1:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    
    return dp[H][W] % MOD