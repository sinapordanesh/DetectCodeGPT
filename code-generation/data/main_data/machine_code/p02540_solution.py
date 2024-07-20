def reachable_cities(N, cities):
    res = []
    for k in range(1, N+1):
        count = 1
        for i in range(1, N+1):
            if i == k:
                continue
            if (cities[k-1][0] > cities[i-1][0] and cities[k-1][1] > cities[i-1][1]) or (cities[k-1][0] < cities[i-1][0] and cities[k-1][1] < cities[i-1][1]):
                count += 1
        res.append(count)
    return res

# Sample Input 1
N = 4
cities = [(1, 4), (2, 3), (3, 1), (4, 2)]
print(*reachable_cities(N, cities))

# Sample Input 2
N = 7
cities = [(6, 4), (4, 3), (3, 5), (7, 1), (2, 7), (5, 2), (1, 6)]
print(*reachable_cities(N, cities))