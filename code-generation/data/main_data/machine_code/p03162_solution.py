def max_total_points_of_happiness(N, activities):
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = activities[0]
    
    for i in range(1, N):
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + activities[i][j])
    
    return max(dp[N-1])

# Sample Input 1
print(max_total_points_of_happiness(3, [[10, 40, 70], [20, 50, 80], [30, 60, 90]]))

# Sample Input 2
print(max_total_points_of_happiness(1, [[100, 10, 1]]))

# Sample Input 3
print(max_total_points_of_happiness(7, [[6, 7, 8], [8, 8, 3], [2, 5, 2], [7, 8, 6], [4, 6, 8], [2, 3, 4], [7, 5, 1]]))