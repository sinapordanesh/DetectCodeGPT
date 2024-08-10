def count_arrangements(N, M):
    MOD = 10**9 + 7
    dp = [0] * (max(N, M) + 1)
    dp[1] = 2
    
    for i in range(2, max(N, M) + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return (2 * dp[N] + 2 * dp[M] - 2) % MOD

N, M = map(int, input().split())
print(count_arrangements(N, M))