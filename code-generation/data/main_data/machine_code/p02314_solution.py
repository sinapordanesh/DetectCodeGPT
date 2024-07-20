def min_coins(n, m, denominations):
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    
    for i in range(1, n+1):
        for j in range(m):
            if denominations[j] <= i:
                dp[i] = min(dp[i], dp[i - denominations[j]] + 1)
    
    return dp[n]

# Sample Input 1
print(min_coins(55, 4, [1, 5, 10, 50]))

# Sample Input 2
print(min_coins(15, 6, [1, 2, 7, 8, 12, 50]))

# Sample Input 3
print(min_coins(65, 6, [1, 2, 7, 8, 12, 50]))