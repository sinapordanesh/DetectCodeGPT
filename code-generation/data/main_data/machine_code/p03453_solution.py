def shortest_paths(N, M, S, T, edges):
    mod = 10**9 + 7
    adj_list = {i: [] for i in range(1, N+1)}
    for u, v, d in edges:
        adj_list[u].append((v, d))
        adj_list[v].append((u, d))
    
    dist_S = [float('inf')] * (N+1)
    dist_S[S] = 0
    dist_T = [float('inf')] * (N+1)
    dist_T[T] = 0
    
    def dijkstra(start, dist):
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, edge_time in adj_list[node]:
                if dist[neighbor] > dist[node] + edge_time:
                    dist[neighbor] = dist[node] + edge_time
                    heapq.heappush(pq, (dist[neighbor], neighbor))
    
    dijkstra(S, dist_S)
    dijkstra(T, dist_T)
    
    min_dist = dist_S[T]
    count = 0
    for i in range(1, N+1):
        for neighbor, edge_time in adj_list[i]:
            if dist_S[i] + edge_time + dist_T[neighbor] > min_dist and dist_S[neighbor] + edge_time + dist_T[i] > min_dist:
                count += 1
    
    return count % mod

# Sample Input 1
N = 4
M = 4
S = 1
T = 3
edges = [(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 1, 1)]
print(shortest_paths(N, M, S, T, edges))