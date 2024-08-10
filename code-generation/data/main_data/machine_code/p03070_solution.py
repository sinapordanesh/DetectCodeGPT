def paint_triangles(num_integers, integers):
    MOD = 998244353
    
    dp = [[[0] * 90001 for _ in range(301)] for _ in range(num_integers + 1)]
    dp[0][0][0] = 1
    
    for i in range(num_integers):
        for j in range(90000):
            for k in range(301):
                dp[i+1][j][k] += dp[i][j][k] * 3
                dp[i+1][j][k] %= MOD
                
                dp[i+1][j+integers[i]][k] += dp[i][j][k]
                dp[i+1][j+integers[i]][k] %= MOD
                
                dp[i+1][j][k+integers[i]] += dp[i][j][k]
                dp[i+1][j][k+integers[i]] %= MOD
                
    ans = 0
    for i in range(1, 90001):
        for j in range(1, 301):
            if i > j and i - j < integers[num_integers-1]:
                ans += dp[num_integers][i][j]
                ans %= MOD
                
    return ans

# Sample Input 1
print(paint_triangles(4, [1, 1, 1, 2]))

# Sample Input 2
print(paint_triangles(6, [1, 3, 2, 3, 5, 2]))

# Sample Input 3
print(paint_triangles(20, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]))