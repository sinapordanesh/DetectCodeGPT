def endless_bfs(N, M, edges):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set([1])
    current = set([1])
    count = 1
    
    while len(visited) != N:
        found = set()
        for v in current:
            for u in graph[v]:
                found.add(u)
        current = found - visited
        visited = visited.union(found)
        
        count += 1
        
        if len(current) == 0:
            return -1
    
    return count

# Sample Test Cases
print(endless_bfs(3, 3, [(1, 2), (1, 3), (2, 3)])) # Output: 2
print(endless_bfs(4, 3, [(1, 2), (2, 3), (3, 4)])) # Output: -1
print(endless_bfs(4, 4, [(1, 2), (2, 3), (3, 4), (4, 1)])) # Output: -1
print(endless_bfs(8, 9, [(2, 1), (3, 5), (1, 6), (2, 5), (3, 1), (8, 4), (2, 7), (7, 1), (7, 4)])) # Output: 3