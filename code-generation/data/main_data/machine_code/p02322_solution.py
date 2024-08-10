def knapsack_limitation(N, W, items):
    dp = [0] * (W + 1)
    for i in range(N):
        v, w, m = items[i]
        for k in range(1, m+1):
            for j in range(W, w*k-1, -1):
                dp[j] = max(dp[j], dp[j - w*k] + v*k)
    return dp[W]

N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

print(knapsack_limitation(N, W, items))