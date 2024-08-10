def LCA(n, nodes, queries):
    def dfs(node, parent):
        ancestors[node] = parent
        for child in nodes[node]:
            dfs(child, node)
    
    def find_lca(u, v):
        u_ancestors = set()
        while u != -1:
            u_ancestors.add(u)
            u = ancestors[u]
        
        while v != -1:
            if v in u_ancestors:
                return v
            v = ancestors[v]
    
    ancestors = [-1] * n
    for i in range(n):
        nodes[i] = nodes[i][1:]
    
    dfs(0, -1)
    
    result = []
    for u, v in queries:
        result.append(find_lca(u, v))
    
    return result

# Sample input
n = 8
nodes = {0: [1, 2, 3], 1: [4, 5], 2: [], 3: [], 4: [6, 7], 5: [], 6: [], 7: []}
queries = [(6, 4), (7, 4), (3, 4), (2, 5)]
print(LCA(n, nodes, queries))