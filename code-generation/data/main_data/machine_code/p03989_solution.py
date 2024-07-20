def solve(N, K):
    MOD = 924844033
    
    dp = [[0] * (N + 2) for _ in range(N + 2)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(N):
            dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j]) % MOD
            if j >= K:
                dp[i][j + 1] = (dp[i][j + 1] - dp[i - 1][j - K]) % MOD
    
    ans = 0
    for i in range(N):
        ans = (ans + dp[N][i]) % MOD
        
    return ans

N, K = map(int, input().split())
print(solve(N, K))