def min_operations(N, edges):
    def dfs(v, p, x):
        ret = x
        for u, w, i in g[v]:
            if u == p:
                continue
            ret ^= w
            ret ^= dfs(u, v, x)
        ans.append((v, p, ret))
        return ret
    
    g = [[] for _ in range(N)]
    for i, (x, y, a) in enumerate(edges):
        g[x].append((y, a, i))
        g[y].append((x, a, i))
        
    ans = []
    dfs(0, -1, 0)
    
    return len([a for v, p, a in ans if p != -1 and a != 0])