def possible_sets(N, K, M):
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        dp[i] = (dp[i-1] * 2) % M
        if i - 2 >= 0:
            dp[i] = (dp[i] + dp[i-2]) % M
        if i + K <= N:
            dp[i] = (dp[i] + dp[i+K]) % M
    return dp[N]

N, K, M = map(int, input().split())
print(possible_sets(N, K, M))