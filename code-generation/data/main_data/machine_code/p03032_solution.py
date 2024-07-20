def max_jewels_sum(N, K, V):
    dp = [[-float('inf')] * (K+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        for k in range(K+1):
            dp[i][k] = max(dp[i][k], dp[i-1][k])

            for j in range(i):
                cost = sum(V[j:i])
                diff = i - j
                if k >= diff:
                    dp[i][k] = max(dp[i][k], dp[j][k-diff] + cost)

    return dp[N][K]

# Input
N, K = map(int, input().split())
V = list(map(int, input().split()))

# Output
print(max_jewels_sum(N, K, V))