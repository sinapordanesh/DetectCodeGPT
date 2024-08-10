def count_triangle_ways(N, sticks):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if len(set([sticks[i], sticks[j], sticks[k]])) == 3 and sticks[i] + sticks[j] > sticks[k] and sticks[j] + sticks[k] > sticks[i] and sticks[k] + sticks[i] > sticks[j]:
                    count += 1
    return count

# Sample Input 1
print(count_triangle_ways(5, [4, 4, 9, 7, 5]))

# Sample Input 2
print(count_triangle_ways(6, [4, 5, 4, 3, 3, 5]))

# Sample Input 3
print(count_triangle_ways(10, [9, 4, 6, 1, 9, 6, 10, 6, 6, 8]))

# Sample Input 4
print(count_triangle_ways(2, [1, 1]))