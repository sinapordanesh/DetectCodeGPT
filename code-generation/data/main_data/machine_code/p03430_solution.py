def highest_possible_value(s, k):
    n = len(s)
    dp = [[0]*(k+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(k+1):
            if s[i-1] == s[-i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 2)
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
    
    return dp[n][k]