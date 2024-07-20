def minimum_cost_flow(V, E, F, edges):
    n = V
    INF = float('inf')
    dist = [INF] * n
    dist[0] = 0
    for i in range(n):
        updated = False
        for u, v, c, d in edges:
            if dist[u] == INF:
                continue
            if dist[u] + d < dist[v] and c > 0:
                dist[v] = dist[u] + d
                updated = True
        if not updated:
            break
    return dist[-1] if dist[-1] != INF else -1

# Sample Input
V = 4
E = 5
F = 2
edges = [(0, 1, 2, 1), (0, 2, 1, 2), (1, 2, 1, 1), (1, 3, 1, 3), (2, 3, 2, 1)]

print(minimum_cost_flow(V, E, F, edges))