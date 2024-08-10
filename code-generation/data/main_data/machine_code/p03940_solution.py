def min_time_to_collect_coins(N, E, T, bears):
    total_time = 0
    for i in range(N):
        total_time += T * i
    return total_time + E

# Sample Input 1
print(min_time_to_collect_coins(3, 9, 1, [1, 3, 8]))

# Sample Input 2
print(min_time_to_collect_coins(3, 9, 3, [1, 3, 8]))

# Sample Input 3
print(min_time_to_collect_coins(2, 1000000000, 1000000000, [1, 999999999]))