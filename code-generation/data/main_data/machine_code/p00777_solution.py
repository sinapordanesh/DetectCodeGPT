def bridge_removal(n, islands, bridges):
    min_time = 0
    for i in range(n-1):
        min_time += 2 * bridges[i]
    return min_time

# Sample Input
print(bridge_removal(4, [1, 2, 3], [10, 20, 30]))
print(bridge_removal(3, [1, 1], [1, 1]))