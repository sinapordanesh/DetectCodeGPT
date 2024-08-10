def single_source_shortest_path(n, graph):
    import heapq
    
    distance = [float('inf')] * n
    distance[0] = 0
    
    pq = [(0, 0)]
    
    while pq:
        dist, u = heapq.heappop(pq)
        
        for i in range(1, len(graph[u]), 2):
            v = graph[u][i-1]
            w = graph[u][i]
            
            if distance[v] > dist + w:
                distance[v] = dist + w
                heapq.heappush(pq, (distance[v], v))
    
    for i in range(n):
        print(i, distance[i])

n = 5
graph = {
    0: [2, 3, 3, 1, 1, 2],
    1: [0, 2, 3, 4],
    2: [0, 3, 3, 1, 4, 1],
    3: [2, 1, 0, 1, 1, 4, 4, 3],
    4: [2, 1, 3, 3]
}

single_source_shortest_path(n, graph)