def find_path(N, M, edges):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
        
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    visited = [False] * (N+1)
    path = []
    
    def dfs(node):
        visited[node] = True
        path.append(node)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(1)
    
    return len(path), path

# Sample Input 1
N1, M1 = 5, 6
edges1 = [(1, 3), (1, 4), (2, 3), (1, 5), (3, 5), (2, 4)]
print(find_path(N1, M1, edges1))

# Sample Input 2
N2, M2 = 7, 8
edges2 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (3, 5), (2, 6)]
print(find_path(N2, M2, edges2))