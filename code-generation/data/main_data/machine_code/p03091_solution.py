def three_circuits(N, M, edges):
    if M != 3*N:
        return "No"
    
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    for i in range(1, N+1):
        if len(adj_list[i]) != 6:
            return "No"
    
    visited = [False] * (N+1)
    def dfs(node, start, count):
        if node == start and count == 6:
            return True
        if visited[node]:
            return False
        
        visited[node] = True
        for neighbor in adj_list[node]:
            if dfs(neighbor, start, count+1):
                return True
        visited[node] = False
        return False
    
    for i in range(1, N+1):
        if not dfs(i, i, 1):
            return "No"
    
    return "Yes"

# Sample Input 1
print(three_circuits(7, 9, [(1, 2), (1, 3), (2, 3), (1, 4), (1, 5), (4, 5), (1, 6), (1, 7), (6, 7)]))

# Sample Input 2
print(three_circuits(3, 3, [(1, 2), (2, 3), (3, 1)]))

# Sample Input 3
print(three_circuits(18, 27, [(17, 7), (12, 15), (18, 17), (13, 18), (13, 6), (5, 7), (7, 1), (14, 5), (15, 11), (7, 6), (1, 9), (5, 4), (18, 16), (4, 6), (7, 2), (7, 11), (6, 3), (12, 14), (5, 2), (10, 5), (7, 8), (10, 15), (3, 15), (9, 8), (7, 15), (5, 16), (18, 15)]))