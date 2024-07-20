def all_pairs_shortest_path(V, E, edges):
    dist = [[float('inf')] * V for _ in range(V)]
    
    for i in range(V):
        dist[i][i] = 0
    
    for u, v, w in edges:
        dist[u][v] = w
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    for i in range(V):
        if dist[i][i] < 0:
            print("NEGATIVE CYCLE")
            return
    
    for i in range(V):
        for j in range(V):
            if dist[i][j] == float('inf'):
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()