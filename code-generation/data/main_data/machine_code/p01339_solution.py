def alien_counting(N, M, rules):
    MOD = 1000000007
    adj = [[] for _ in range(N)]
    for s, d in rules:
        adj[s-1].append(d-1)
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        for j in range(N):
            for k in adj[j]:
                dp[j] += dp[k]
                dp[j] %= MOD
    return sum(dp) % MOD

# Sample Input 1
print(alien_counting(5, 4, [(2, 3), (3, 4), (4, 3), (5, 4)]))

# Sample Input 2
print(alien_counting(5, 5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]))

# Sample Input 3
print(alien_counting(5, 0, []))