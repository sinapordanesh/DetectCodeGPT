from heapq import heappush, heappop

def min_total_weight(N, M, edges, Q, queries):
    graph = {i: [] for i in range(1, N+1)}
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    dist = [[float('inf')] * N for _ in range(N)]
    
    for i in range(1, N+1):
        dist[i-1][i-1] = 0
        pq = [(0, i)]
        while pq:
            d, node = heappop(pq)
            if dist[i-1][node-1] < d:
                continue
            for neighbor, weight in graph[node]:
                if d + weight < dist[i-1][neighbor-1]:
                    dist[i-1][neighbor-1] = d + weight
                    heappush(pq, (d + weight, neighbor))
                
    result = []
    for s, t in queries:
        result.append(dist[s-1][t-1])
    
    return result

# Sample Input 1
N1 = 4
M1 = 3
edges1 = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
Q1 = 2
queries1 = [(2, 3), (1, 4)]

print(*min_total_weight(N1, M1, edges1, Q1, queries1))

# Sample Input 2
N2 = 4
M2 = 6
edges2 = [(1, 3, 5), (4, 1, 10), (2, 4, 6), (3, 2, 2), (3, 4, 5), (2, 1, 3)]
Q2 = 1
queries2 = [(2, 3)]

print(*min_total_weight(N2, M2, edges2, Q2, queries2))