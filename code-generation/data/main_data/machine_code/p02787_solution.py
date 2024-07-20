def min_magic_points(H, N, spells):
    dp = [float('inf')] * (H+1)
    dp[0] = 0
    
    for i in range(1, H+1):
        for j in range(N):
            if i - spells[j][0] >= 0:
                dp[i] = min(dp[i], dp[i - spells[j][0]] + spells[j][1])
    
    return dp[H]

# Sample Input 1
print(min_magic_points(9, 3, [(8, 3), (4, 2), (2, 1)]))

# Sample Input 2
print(min_magic_points(100, 6, [(1, 1), (2, 3), (3, 9), (4, 27), (5, 81), (6, 243)]))

# Sample Input 3
print(min_magic_points(9999, 10, [(540, 7550), (691, 9680), (700, 9790), (510, 7150), (415, 5818), (551, 7712), (587, 8227), (619, 8671), (588, 8228), (176, 2461)]))