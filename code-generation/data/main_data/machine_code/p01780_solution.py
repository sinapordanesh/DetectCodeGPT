def bfs_foxpower(n, parents):
    distance = [0] * n
    for i in range(1, n):
        distance[i] = distance[parents[i-1]-1] + 1
    return sum(distance)

# Sample Input 1
print(bfs_foxpower(4, [1, 1, 2]))

# Sample Input 2
print(bfs_foxpower(4, [1, 1, 3]))

# Sample Input 3
print(bfs_foxpower(11, [1, 1, 3, 3, 2, 4, 1, 3, 2, 9]))