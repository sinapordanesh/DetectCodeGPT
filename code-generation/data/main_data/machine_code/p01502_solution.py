def min_cost_sightseeing_tour(N, C):
    import itertools
    min_cost = float('inf')
    for perm in itertools.permutations(range(N)):
        cost = 0
        for i in range(N-1):
            cost += C[perm[i]][perm[i+1]]
        min_cost = min(min_cost, cost)
    return min_cost

# Sample Input
N = 3
C = [[0, 2, 7], [2, 0, 4], [5, 8, 0]]
print(min_cost_sightseeing_tour(N, C))