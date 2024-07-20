def minimum_cost_arborescence(V, E, r, edges):
    import sys
    
    def bellman_ford():
        dist = [sys.maxsize] * V
        dist[r] = 0
        for _ in range(V):
            changed = False
            for s, t, w in edges:
                if dist[s] != sys.maxsize and dist[t] > dist[s] + w:
                    dist[t] = dist[s] + w
                    changed = True
            if not changed:
                break
        return dist
    
    dist = bellman_ford()
    return sum(dist)

# Sample Input 1
V, E, r = 4, 6, 0
edges = [(0, 1, 3), (0, 2, 2), (2, 0, 1), (2, 3, 1), (3, 0, 1), (3, 1, 5)]
print(minimum_cost_arborescence(V, E, r, edges))

# Sample Input 2
V, E, r = 6, 10, 0
edges = [(0, 2, 7), (0, 1, 1), (0, 3, 5), (1, 4, 9), (2, 1, 6), (1, 3, 2), (3, 4, 3), (4, 2, 2), (2, 5, 8), (3, 5, 3)]
print(minimum_cost_arborescence(V, E, r, edges))