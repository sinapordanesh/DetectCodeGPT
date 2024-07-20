def shortest_path(N, edges, Q, K, queries):
    import heapq
    
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    
    for edge in edges:
        a, b, c = edge
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))
    
    def dijkstra(start, end):
        pq = [(0, start)]
        dist = {v: float('inf') for v in adj_list}
        dist[start] = 0
        
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            
            for neighbor, edge_len in adj_list[node]:
                if d + edge_len < dist[neighbor]:
                    dist[neighbor] = d + edge_len
                    heapq.heappush(pq, (d + edge_len, neighbor))
        
        return dist[end]
    
    result = []
    for query in queries:
        x, y = query
        result.append(dijkstra(x, K) + dijkstra(K, y))
    
    return result

# Sample Input 1
N = 5
edges = [(1, 2, 1), (1, 3, 1), (2, 4, 1), (3, 5, 1)]
Q = 3
K = 2
queries = [(3, 1), (2, 4), (2, 3)]
print(*shortest_path(N, edges, Q, K, queries))

# Sample Input 2
N = 7
edges = [(1, 2, 1), (1, 3, 3), (1, 4, 5), (1, 5, 7), (1, 6, 9), (1, 7, 11)]
Q = 4
K = 2
queries = [(3, 2), (1, 3), (4, 5), (6, 7)]
print(*shortest_path(N, edges, Q, K, queries))

# Sample Input 3
N = 10
edges = [(1, 2, 1000000000), (2, 3, 1000000000), (3, 4, 1000000000), (4, 5, 1000000000), 
         (5, 6, 1000000000), (6, 7, 1000000000), (7, 8, 1000000000), (8, 9, 1000000000), (9, 10, 1000000000)]
Q = 2
K = 1
queries = [(1, 1), (9, 10)]
print(*shortest_path(N, edges, Q, K, queries))