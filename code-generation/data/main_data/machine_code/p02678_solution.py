def place_signposts(N, M, passages):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    
    for passage in passages:
        A, B = passage
        graph[A].append(B)
        graph[B].append(A)
    
    signposts = [0] * N
    visited = [False] * (N+1)
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                signposts[neighbor-1] = node
                dfs(neighbor)
    
    dfs(1)
    
    print("Yes")
    for i in range(1, N):
        print(signposts[i])
        
# Sample Input
N = 4
M = 4
passages = [(1, 2), (2, 3), (3, 4), (4, 2)]

place_signposts(N, M, passages)