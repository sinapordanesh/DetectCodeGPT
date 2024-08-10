from heapq import heappush, heappop

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while heap:
        (current_distance, current_node) = heappop(heap)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(heap, (distance, neighbor))
    
    return distances

def count_edges_not_in_shortest_path(N, M, edges):
    graph = {i: {} for i in range(1, N+1)}
    
    for a, b, c in edges:
        graph[a][b] = c
        graph[b][a] = c
    
    result = 0
    
    for i in range(1, N+1):
        distances = dijkstra(graph, i)
        
        for j in range(i+1, N+1):
            for k in range(1, N+1):
                if k != i and k != j:
                    if distances[j] == distances[k] + graph[k][j] or distances[j] == distances[k]:
                        break
            else:
                result += 1
    
    return result

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

print(count_edges_not_in_shortest_path(N, M, edges))