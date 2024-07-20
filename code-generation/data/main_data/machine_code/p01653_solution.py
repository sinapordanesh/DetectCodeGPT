def smallest_gap(N, M, S1, S2, T, bridges):
    import heapq
    
    graph = {i: [] for i in range(1, N+1)}
    for a, b, w in bridges:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    def dijkstra(start):
        distance = {node: float('inf') for node in graph}
        distance[start] = 0
        queue = [(0, start)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distance[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                new_distance = current_distance + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))
        
        return distance
    
    dist_S1 = dijkstra(S1)
    dist_S2 = dijkstra(S2)
    dist_T = dijkstra(T)
    
    min_gap = float('inf')
    for i in range(1, N+1):
        gap = abs(dist_S1[i] - dist_T[i]) - abs(dist_S2[i] - dist_T[i])
        min_gap = min(min_gap, gap)
    
    return min_gap

# Sample Input
print(smallest_gap(3, 2, 2, 3, 1, [(1, 2, 1), (1, 3, 2)]))
print(smallest_gap(4, 3, 1, 4, 2, [(2, 1, 3), (2, 3, 'x'), (4, 3, 'x')]))