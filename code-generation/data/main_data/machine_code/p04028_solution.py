def count_ways_to_press_keys(N, s):
    MOD = 10**9 + 7
    dp = [[0] * (N+1) for _ in range(len(s)+1)]
    dp[0][0] = 1
    
    for i in range(1, len(s)+1):
        for j in range(N+1):
            if (j > 0 and s[i-1] == '0'):
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] += dp[i-1][j] * 2
            dp[i][j] %= MOD
    
    return dp[-1][N] % MOD