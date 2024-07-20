def find_smallest_cost(N, T, routes):
    min_cost = float('inf')
    for i in range(N):
        if routes[i][1] <= T:
            min_cost = min(min_cost, routes[i][0])
    
    if min_cost == float('inf'):
        return "TLE"
    else:
        return min_cost