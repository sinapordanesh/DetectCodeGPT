def knapsack_problem(N, W, items):
    dp = [0] * (W + 1)
    
    for i in range(N):
        for j in range(W, items[i][0] - 1, -1):
            dp[j] = max(dp[j], dp[j - items[i][0]] + items[i][1])
    
    return dp[W]

# Sample Input
N = 4
W = 6
items = [(2, 1), (3, 4), (4, 10), (3, 4)]
print(knapsack_problem(N, W, items))