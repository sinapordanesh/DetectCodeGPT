def min_bridges_removed(N, M, requests):
    graph = {i: [] for i in range(1, N+1)}
    for a, b in requests:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node, parent):
        bridges_removed = 0
        for neighbor in graph[node]:
            if neighbor != parent:
                bridges_removed += dfs(neighbor, node)
        if bridges_removed == 0 and node != 1:
            return 1
        return bridges_removed
    
    return dfs(1, -1) - 1