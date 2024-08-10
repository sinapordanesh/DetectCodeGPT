def dfs(adj_list):
    def explore(v):
        nonlocal time
        visited[v] = True
        time += 1
        discover[v] = time
        
        for neighbor in adj_list[v]:
            if not visited[neighbor]:
                explore(neighbor)
        
        time += 1
        finish[v] = time
    
    n = len(adj_list)
    visited = [False] * n
    discover = [0] * n
    finish = [0] * n
    time = 0
    
    for vertex in range(n):
        if not visited[vertex]:
            explore(vertex)
    
    for i in range(n):
        print(i+1, discover[i], finish[i])