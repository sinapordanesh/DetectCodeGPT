def longest_common_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[""] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + s[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
    
    return dp[m][n]