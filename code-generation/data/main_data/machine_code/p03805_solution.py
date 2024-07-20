def count_paths(N, M, edges):
    graph = {}
    for i in range(1, N+1):
        graph[i] = set()
    
    for edge in edges:
        a, b = edge
        graph[a].add(b)
        graph[b].add(a)
    
    def dfs(node, visited):
        visited.add(node)
        if len(visited) == N:
            return 1
        
        count = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                count += dfs(neighbor, visited.copy())
        
        return count
    
    return dfs(1, set())

# Sample Input 1
N1, M1 = 3, 3
edges1 = [(1, 2), (1, 3), (2, 3)]
print(count_paths(N1, M1, edges1))

# Sample Input 2
N2, M2 = 7, 7
edges2 = [(1, 3), (2, 7), (3, 4), (4, 5), (4, 6), (5, 6), (6, 7)]
print(count_paths(N2, M2, edges2))