def has_even_tree(N, M, queries):
    edges = {}
    for a, b in queries:
        if a not in edges:
            edges[a] = []
        if b not in edges:
            edges[b] = []
        edges[a].append(b)
        edges[b].append(a)
    
    visited = [False] * (N + 1)
    
    def dfs(node):
        visited[node] = True
        count = 1
        for neighbor in edges[node]:
            if not visited[neighbor]:
                count += dfs(neighbor)
        return count
    
    if dfs(1) == N:
        return "YES"
    else:
        return "NO"