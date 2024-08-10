def share_candies(N, K, a):
    MOD = 10**9 + 7
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(K+1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j] - (dp[i-1][j-(a[i-1]+1)] if j-(a[i-1]+1) >= 0 else 0)) % MOD
    
    return dp[N][K]

N, K = map(int, input().split())
a = list(map(int, input().split()))

print(share_candies(N, K, a))