def minimum_required_fare(N, M, lines):
    import heapq
    
    graph = {i: [] for i in range(1, N+1)}
    for p, q, c in lines:
        graph[p].append((q, c))
        graph[q].append((p, c))
    
    dist = {i: float('inf') for i in range(1, N+1)}
    dist[1] = 0
    pq = [(0, 1, 0)]
    
    while pq:
        fare, node, company = heapq.heappop(pq)
        if node == N:
            return fare
        
        for neighbor, neighbor_company in graph[node]:
            new_fare = fare + (neighbor_company != company)
            if new_fare < dist[neighbor]:
                dist[neighbor] = new_fare
                heapq.heappush(pq, (new_fare, neighbor, neighbor_company))
    
    return -1

# Sample Input 1
print(minimum_required_fare(3, 3, [(1, 2, 1), (2, 3, 1), (3, 1, 2)]))

# Sample Input 2
print(minimum_required_fare(8, 11, [(1, 3, 1), (1, 4, 2), (2, 3, 1), (2, 5, 1), (3, 4, 3), (3, 6, 3), (3, 7, 3), (4, 8, 4), (5, 6, 1), (6, 7, 5), (7, 8, 5)]))

# Sample Input 3
print(minimum_required_fare(2, 0, []))