from heapq import heappop, heappush

def shortest_path(N, M, operations):
    graph = {i: [] for i in range(1, N+1)}
    
    for L, R, C in operations:
        for i in range(L, R):
            for j in range(i+1, R):
                graph[i].append((j, C))
                graph[j].append((i, C))
    
    dist = {i: float('inf') for i in range(1, N+1)}
    dist[1] = 0
    
    pq = [(0, 1)]
    
    while pq:
        d, node = heappop(pq)
        
        if d > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heappush(pq, (dist[neighbor], neighbor))
    
    return dist[N] if dist[N] != float('inf') else -1

# Input
N, M = map(int, input().split())
operations = [tuple(map(int, input().split())) for _ in range(M)]

# Output
print(shortest_path(N, M, operations))