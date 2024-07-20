def find_number_of_bridges(N, M, edges):
    def dfs(u, p):
        low[u] = pre[u] = dfs.counter
        dfs.counter += 1
        for v in adj[u]:
            if pre[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > pre[u]:
                    bridges.add((min(u, v), max(u, v)))
            elif v != p:
                low[u] = min(low[u], pre[v])
    
    adj = [[] for _ in range(N)]
    for a, b in edges:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    
    pre = [-1] * N
    low = [-1] * N
    dfs.counter = 0
    bridges = set()
    
    dfs(0, -1)
    
    return len(bridges)