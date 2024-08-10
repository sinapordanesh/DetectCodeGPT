def max_D(N, X, cities):
    max_distance = 0
    for city in cities:
        distance = abs(city - X)
        max_distance = max(max_distance, distance)
    return max_distance