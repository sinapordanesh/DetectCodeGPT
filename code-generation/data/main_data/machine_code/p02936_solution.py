def tree_counters(N, Q, edges, operations):
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
    
    counters = [0] * N
    
    def dfs(node, parent):
        counters[node] += counters[parent]
        for child in adj_list[node]:
            if child != parent:
                dfs(child, node)
    
    for p, x in operations:
        counters[p-1] += x
    
    dfs(0, 0)
    
    return ' '.join(map(str, counters))