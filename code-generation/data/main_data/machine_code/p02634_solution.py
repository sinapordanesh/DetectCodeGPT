def paint_ways(A, B, C, D):
    MOD = 998244353
    dp = [[0] * (D + 1) for _ in range(C + 1)]
    dp[A][B] = 1

    for i in range(A, C + 1):
        for j in range(B, D + 1):
            if i == A and j == B:
                continue
            dp[i][j] = (dp[i-1][j] * (j-B+1) + dp[i][j-1] * (i-A+1)) % MOD

    return dp[C][D] 

# Sample Input 1
print(paint_ways(1, 1, 2, 2))

# Sample Input 2
print(paint_ways(2, 1, 3, 4))

# Sample Input 3
print(paint_ways(31, 41, 59, 265))