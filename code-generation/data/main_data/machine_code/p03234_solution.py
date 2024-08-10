def connected_parts(N, K, pairs):
    MOD = 10**9 + 7
    total_connected_parts = 0
    
    def dfs(i, visited, adj_list):
        visited[i] = True
        for neighbor in adj_list[i]:
            if not visited[neighbor]:
                dfs(neighbor, visited, adj_list)
    
    for i in range(1, 2*N+1):
        adj_list = {x: [] for x in range(1, 2*N+1)}
        for j in range(1, 2*N+1):
            if i != j:
                adj_list[j].append(j+1)
                adj_list[j+1].append(j)
        
        for pair in pairs:
            if i == pair[0] or i == pair[1]:
                adj_list[pair[0]].append(pair[1])
                adj_list[pair[1]].append(pair[0])
        
        visited = {x: False for x in range(1, 2*N+1)}
        components = 0
        for k in range(1, 2*N+1):
            if not visited[k]:
                dfs(k, visited, adj_list)
                components += 1
        
        total_connected_parts += components
    
    return total_connected_parts % MOD

# Sample Input 1
print(connected_parts(2, 0, []))

# Sample Input 2
print(connected_parts(4, 2, [(5, 2), (6, 1)]))

# Sample Input 3
print(connected_parts(20, 10, [(10, 18), (11, 17), (14, 7), (4, 6), (30, 28), (19, 24), (29, 22), (25, 32), (38, 34), (36, 39)]))