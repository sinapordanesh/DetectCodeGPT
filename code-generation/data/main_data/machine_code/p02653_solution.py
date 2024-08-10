def count_strings(N, A, B):
    MOD = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    
    for i in range(1, N+1):
        for j in range(1, min(i, A)+1):
            dp[i] += dp[i-j]
            dp[i] %= MOD
        for j in range(1, min(i, B)+1):
            dp[i] += dp[i-j]
            dp[i] %= MOD
            
    return dp[N]

N, A, B = map(int, input().split())
print(count_strings(N, A, B))