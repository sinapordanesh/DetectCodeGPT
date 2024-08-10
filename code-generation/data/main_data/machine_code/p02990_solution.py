def arrange_balls(N, K):
    MOD = 10**9 + 7
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        dp[i][0] = 1
        for j in range(1, min(i, K) + 1):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD
    
    res = [0] * K
    for i in range(1, K + 1):
        res[i-1] = dp[N][i]
    
    return res

N, K = map(int, input().split())
for num in arrange_balls(N, K):
    print(num)