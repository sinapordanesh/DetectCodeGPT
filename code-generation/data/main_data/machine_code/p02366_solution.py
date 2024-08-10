def articulation_points(graph):
    def dfs(node, parent, visited, disc, low, res):
        visited[node] = True
        disc[node] = dfs.timer
        low[node] = dfs.timer
        dfs.timer += 1
        children = 0
        for neighbor in graph[node]:
            if not visited[neighbor]:
                children += 1
                dfs(neighbor, node, visited, disc, low, res)
                low[node] = min(low[node], low[neighbor])
                if parent != -1 and low[neighbor] >= disc[node]:
                    res.add(node)
            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])
        if parent == -1 and children > 1:
            res.add(node)
    
    n = len(graph)
    visited = [False] * n
    disc = [float('inf')] * n
    low = [float('inf')] * n
    dfs.timer = 0
    res = set()
    
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, visited, disc, low, res)
    
    return sorted(res)