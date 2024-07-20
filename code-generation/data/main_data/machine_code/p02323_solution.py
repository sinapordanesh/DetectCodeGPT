from itertools import permutations

def traveling_salesman_problem(V, E, edges):
    graph = {i: {} for i in range(V)}
    for s, t, d in edges:
        graph[s][t] = d
    
    min_distance = float('inf')
    for path in permutations(range(V)):
        distance = 0
        for i in range(V-1):
            if path[i+1] in graph[path[i]]:
                distance += graph[path[i]][path[i+1]]
            else:
                distance = float('inf')
                break
        if path[0] in graph[path[-1]]:
            distance += graph[path[-1]][path[0]]
        else:
            distance = float('inf')
        min_distance = min(min_distance, distance)

    return min_distance if min_distance != float('inf') else -1

# Sample Input 1
V1 = 4
E1 = 6
edges1 = [(0, 1, 2), (1, 2, 3), (1, 3, 9), (2, 0, 1), (2, 3, 6), (3, 2, 4)]
print(traveling_salesman_problem(V1, E1, edges1))

# Sample Input 2
V2 = 3
E2 = 3
edges2 = [(0, 1, 1), (1, 2, 1), (0, 2, 1)]
print(traveling_salesman_problem(V2, E2, edges2))