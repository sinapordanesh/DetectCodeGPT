def min_total_distance(N, K, x):
    x.sort()
    total_distance = 0
    for i in range(N):
        total_distance += min(x[i], K-x[i]) * 2
    return total_distance

# Sample Input 1
print(min_total_distance(1, 10, [2])) # Output: 4

# Sample Input 2
print(min_total_distance(2, 9, [3, 6])) # Output: 12

# Sample Input 3
print(min_total_distance(5, 20, [11, 12, 9, 17, 12])) # Output: 74