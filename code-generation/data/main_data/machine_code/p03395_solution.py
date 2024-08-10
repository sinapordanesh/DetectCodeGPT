def min_cost(N, a, b):
    import numpy as np
    
    dp = np.zeros((N+1, 51), dtype=np.int64)
    
    for i in range(1, N+1):
        for j in range(51):
            dp[i][j] = 2**j
    
    for i in range(1, N+1):
        for j in range(51):
            for k in range(51):
                dp[i][(j*k)%51] = min(dp[i][(j*k)%51], dp[i-1][j] + abs(b[i-1] - (a[i-1] % k)))
    
    return dp[N][0] if dp[N][0] < 2**50 else -1

# Sample Input 1
print(min_cost(3, [19, 10, 14], [0, 3, 4]))

# Sample Input 2
print(min_cost(3, [19, 15, 14], [0, 0, 0]))

# Sample Input 3
print(min_cost(2, [8, 13], [5, 13]))

# Sample Input 4
print(min_cost(4, [2, 0, 1, 8], [2, 0, 1, 8]))

# Sample Input 5
print(min_cost(1, [50], [13]))