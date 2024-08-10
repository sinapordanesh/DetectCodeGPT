def knapsack(N, W, values, weights):
    dp = [0] * (W + 1)
    for i in range(N):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]