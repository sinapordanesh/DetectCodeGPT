def permutation_oddness(n, k):
    MOD = 10**9 + 7
    
    dp = [[0] * (n*n+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(n*n):
            for d in range(n):
                if j + d <= n*n:
                    dp[i+1][j+d] += dp[i][j]
                    dp[i+1][j+d] %= MOD
    
    return dp[n][k]

n, k = map(int, input().split())
print(permutation_oddness(n, k))