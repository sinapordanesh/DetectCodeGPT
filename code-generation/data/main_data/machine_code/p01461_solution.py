def shortest_time(N, branching_points):
    dp = [0] * N
    for i in range(N-1, 0, -1):
        dp[i] = 1 + max(dp[branching_points[i-1][0]], dp[branching_points[i-1][1]])
    return dp[1] + 1

# Sample Input 1
N = 4
branching_points = [(2, 3), (4, 4), (4, 4)]
print(shortest_time(N, branching_points))

# Sample Input 2
N = 5
branching_points = [(5, 2), (3, 5), (5, 4), (5, 5)]
print(shortest_time(N, branching_points))