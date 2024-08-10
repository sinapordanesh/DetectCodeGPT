def divide_pairs(N, A, B, C):
    MOD = 10**9 + 7
    dp = [[0] * (N+1) for _ in range(4)]
    dp[0][0] = 1
    
    for i in range(1, 2*N+1):
        dp[0] = dp[1]
        dp[1] = dp[2]
        dp[2] = dp[3]
        dp[3] = [0] * (N+1)
        
        for j in range(1, N+1):
            dp[3][j] = dp[3][j-1]
            if j > A:
                dp[3][j] = (dp[3][j] + dp[0][j-A-1]) % MOD
            if j > B:
                dp[3][j] = (dp[3][j] + dp[1][j-B-1]) % MOD
            if j > C:
                dp[3][j] = (dp[3][j] + dp[2][j-C-1]) % MOD
            
    return dp[3][N]

N, A, B, C = map(int, input().split())
print(divide_pairs(N, A, B, C))