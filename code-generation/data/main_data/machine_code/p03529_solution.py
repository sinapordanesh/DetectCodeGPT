def min_score(N, K):
    MOD = 1000000007
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = (j * dp[i-1][j-1] + (i-j+1) * dp[i-1][j]) % MOD
    
    total = sum(dp[N])
    return total % MOD

N, K = map(int, input().split())
print(min_score(N, K))