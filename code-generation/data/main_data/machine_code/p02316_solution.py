def knapsack(N, W, items):
    dp = [0] * (W + 1)
    for i in range(1, W + 1):
        for v, w in items:
            if w <= i:
                dp[i] = max(dp[i], dp[i - w] + v)
    return dp[W]

N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
print(knapsack(N, W, items))