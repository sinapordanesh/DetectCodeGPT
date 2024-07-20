def num_roads_connected(N, M, roads):
    cities = [0] * N
    for a, b in roads:
        cities[a-1] += 1
        cities[b-1] += 1
    
    return cities

# Sample Input 1
N, M = 4, 3
roads = [(1, 2), (2, 3), (1, 4)]
print(*num_roads_connected(N, M, roads))

# Sample Input 2
N, M = 2, 5
roads = [(1, 2), (2, 1), (1, 2), (2, 1), (1, 2)]
print(*num_roads_connected(N, M, roads))

# Sample Input 3
N, M = 8, 8
roads = [(1, 2), (3, 4), (1, 5), (2, 8), (3, 7), (5, 2), (4, 1), (6, 8)]
print(*num_roads_connected(N, M, roads))