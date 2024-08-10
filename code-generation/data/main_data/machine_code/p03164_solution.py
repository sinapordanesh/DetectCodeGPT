def knapsack(N, W, items):
    dp = [0] * (W + 1)
    for i in range(N):
        weight, value = items[i]
        for w in range(W, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[W]

# Input
N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

# Output
print(knapsack(N, W, items))