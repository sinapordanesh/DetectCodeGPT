def max_distance_squirrels(N, edges):
    MOD = 10**9 + 7
    
    adj_list = {i:[] for i in range(1, N+1)}
    for x, y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    subtree_size = [0] * (N+1)
    total_nodes = [0] * (N+1)
    
    def dfs(node, parent):
        total_nodes[node] = 1
        for child in adj_list[node]:
            if child != parent:
                dfs(child, node)
                total_nodes[node] += total_nodes[child]
    
    dfs(1, -1)
    
    for i in range(1, N+1):
        subtree_size[i] = total_nodes[i]
    
    res = 1
    for i in range(1, N+1):
        res = (res * i) % MOD
    
    print(res)

# Sample Input
N = 3
edges = [(1, 2), (2, 3)]
max_distance_squirrels(N, edges)