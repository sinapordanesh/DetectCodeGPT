def knapsack_problem(N, W, items):
    dp = [0] * (W + 1)
    for i in range(1, N + 1):
        for j in range(W, 0, -1):
            if items[i - 1][1] <= j:
                dp[j] = max(dp[j], dp[j - items[i - 1][1]] + items[i - 1][0])
    return dp[W]

N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w = map(int, input().split())
    items.append((v, w))

print(knapsack_problem(N, W, items))