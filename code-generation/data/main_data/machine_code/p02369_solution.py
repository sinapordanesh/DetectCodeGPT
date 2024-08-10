def has_cycle(V, E, edges):
    def dfs(node, visited, stack):
        visited[node] = True
        stack[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True
        
        stack[node] = False
        return False
    
    graph = {i: [] for i in range(V)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    visited = [False] * V
    stack = [False] * V
    
    for node in range(V):
        if not visited[node]:
            if dfs(node, visited, stack):
                return 1
    return 0

# Sample Input
print(has_cycle(3, 3, [(0, 1), (0, 2), (1, 2)]))
print(has_cycle(3, 3, [(0, 1), (1, 2), (2, 0)]))