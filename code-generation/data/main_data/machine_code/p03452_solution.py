def consistent_people(N, M, info):
    graph = {}
    for i in range(1, N + 1):
        graph[i] = []
    
    for i in range(M):
        L, R, D = info[i]
        graph[L].append((R, D))
        graph[R].append((L, -D))
    
    visited = [False] * (N + 1)
    positions = [0] * (N + 1)
    
    def dfs(node, pos):
        if visited[node]:
            return
        visited[node] = True
        positions[node] = pos
        for neighbor, diff in graph[node]:
            dfs(neighbor, pos + diff)
    
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i, 0)
    
    for i in range(1, N + 1):
        for neighbor, diff in graph[i]:
            if positions[neighbor] != positions[i] + diff:
                return "No"
    
    return "Yes"  