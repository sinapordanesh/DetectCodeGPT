def knight_ways(X, Y):
    MOD = 10**9 + 7
    dp = [[0] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 1
    
    for i in range(X + 1):
        for j in range(Y + 1):
            if i + 1 <= X and j + 2 <= Y:
                dp[i + 1][j + 2] = (dp[i + 1][j + 2] + dp[i][j]) % MOD
            if i + 2 <= X and j + 1 <= Y:
                dp[i + 2][j + 1] = (dp[i + 2][j + 1] + dp[i][j]) % MOD
                
    return dp[X][Y] % MOD