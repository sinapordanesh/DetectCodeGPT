def solve_tree_problem(N, edges):
    mod = 924844033
    
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
    
    def dfs(v, parent):
        subtree_size[v] = 1
        for u in adj_list[v]:
            if u != parent:
                dfs(u, v)
                subtree_size[v] += subtree_size[u]
    
    def dp(v, parent):
        res = 1
        for u in adj_list[v]:
            if u != parent:
                res = (res * dp(u, v) * inv[subtree_size[u]]) % mod
        return res * fact[subtree_size[v]-1] % mod
    
    fact = [1] * N
    for i in range(2, N):
        fact[i] = fact[i-1] * i % mod
    
    inv = [1] * N
    inv[N-1] = pow(fact[N-1], mod-2, mod)
    for i in range(N-2, -1, -1):
        inv[i] = inv[i+1] * (i+1) % mod
    
    subtree_size = [0] * N
    res = [0] * N
    for k in range(1, N+1):
        dfs(0, -1)
        res[k-1] = dp(0, -1)
    
    return res

# Sample Input 1
N = 3
edges = [(1, 2), (2, 3)]
print(*solve_tree_problem(N, edges))

# Sample Input 2
N = 4
edges = [(1, 2), (1, 3), (1, 4)]
print(*solve_tree_problem(N, edges))

# Sample Input 3
N = 7
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6), (6, 7)]
print(*solve_tree_problem(N, edges))