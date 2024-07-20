def optimal_bst(keys, p_values, q_values):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = q_values[i]
    
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            sum_ = sum(p_values[i:j+1]) + sum(q_values[i:j+1])
            for r in range(i, j+1):
                cost = sum_ + (dp[i][r-1] if r > i else 0) + (dp[r+1][j] if r < j else 0)
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n-1]