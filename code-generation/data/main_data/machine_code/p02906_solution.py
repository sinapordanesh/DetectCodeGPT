def check_graph(N, M, Q, clues):
    graph = [[] for _ in range(N)]
    
    for a, b, c in clues:
        if c == 0:
            graph[a].append(b)
            graph[b].append(a)
    
    for i in range(N):
        visited = [False] * N
        stack = [i]
        count = 0
        
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            count += 1
            stack.extend([x for x in graph[node] if not visited[x]])
        
        if count != N:
            return "No"
    
    return "Yes"

# Input
N, M, Q = map(int, input().split())
clues = [list(map(int, input().split())) for _ in range(Q)]

# Calling the function
print(check_graph(N, M, Q, clues))