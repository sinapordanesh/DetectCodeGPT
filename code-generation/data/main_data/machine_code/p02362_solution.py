def bellman_ford(V, E, r, edges):
    dist = [float('inf')] * V
    dist[r] = 0
    
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return "NEGATIVE CYCLE"
    
    return '\n'.join(["INF" if d == float('inf') else str(d) for d in dist])