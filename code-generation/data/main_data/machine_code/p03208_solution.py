def min_height_diff(N, K, heights):
    heights.sort()
    min_diff = float('inf')
    for i in range(N - K + 1):
        min_diff = min(min_diff, heights[i+K-1] - heights[i])
    return min_diff

# Sample Input 1
print(min_height_diff(5, 3, [10, 15, 11, 14, 12]))

# Sample Input 2
print(min_height_diff(5, 3, [5, 7, 5, 7, 7]))