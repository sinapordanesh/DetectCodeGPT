def max_leaflets(Q, cases):
    MOD = 1000000007
    
    for i in range(Q):
        N, C = cases[i]
        
        dp = [0] * (N + 1)
        dp[0] = 1
        
        for j in range(1, N + 1):
            dp[j] += dp[j - 1]
            dp[j] %= MOD
            
            if j >= C:
                dp[j] += dp[j - C]
                dp[j] %= MOD
                
        print(dp[N])

# Sample input
max_leaflets(2, [(20, 8), (20, 12)])