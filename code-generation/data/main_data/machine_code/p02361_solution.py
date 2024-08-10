def single_source_shortest_path(graph, source):
    import heapq
    
    distances = [float('inf')] * len(graph)
    distances[source] = 0
    
    pq = [(0, source)]
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    for i in range(len(distances)):
        if distances[i] == float('inf'):
            print("INF")
        else:
            print(distances[i])