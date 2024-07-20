def knapsack_with_limitations(N, W, items):
    dp = [0] * (W + 1)
    
    for i in range(N):
        v, w, m = items[i]
        for j in range(W, w - 1, -1):
            for k in range(1, m + 1):
                if j - k * w >= 0:
                    dp[j] = max(dp[j], dp[j - k * w] + k * v)
    
    return dp[W] if W > 0 else 0

# Sample Input 1
N = 4
W = 8
items = [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]
print(knapsack_with_limitations(N, W, items))

# Sample Input 2
N = 2
W = 100
items = [(1, 1, 100), (2, 1, 50)]
print(knapsack_with_limitations(N, W, items))