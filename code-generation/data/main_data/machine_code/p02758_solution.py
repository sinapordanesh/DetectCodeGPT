def robot_sets(N, robots):
    MOD = 998244353
    
    robots.sort()
    
    dp = [0] * (N + 1)
    dp[N] = 1
    
    for i in range(N - 1, -1, -1):
        dp[i] = dp[i + 1]
        j = i + 1
        while j < N and robots[j][0] < robots[i][0] + robots[i][1]:
            dp[i] += dp[j + 1]
            dp[i] %= MOD
            j += 1
    
    return dp[0] % MOD

# Sample Input 1
print(robot_sets(2, [(1, 5), (3, 3)]))

# Sample Input 2
print(robot_sets(3, [(6, 5), (-1, 10), (3, 3)]))

# Sample Input 3
print(robot_sets(4, [(7, 10), (-10, 3), (4, 3), (-4, 3)]))

# Sample Input 4
print(robot_sets(20, [(-8, 1), (26, 4), (0, 5), (9, 1), (19, 4), (22, 20), (28, 27), (11, 8), (-3, 20), (-25, 17), 
                      (10, 4), (-18, 27), (24, 28), (-11, 19), (2, 27), (-2, 18), (-1, 12), (-24, 29), (31, 29), (29, 7)]))