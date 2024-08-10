def min_operations_to_gather(N, S, edges):
    def dfs(v, p):
        nonlocal ans
        cnt = 0
        for u in adj[v]:
            if u == p:
                continue
            cnt += dfs(u, v)
        if cnt == 0:
            cnt = S[v]
        if cnt > 1:
            ans += cnt - 1
            cnt = 1
        return cnt
    
    adj = {i: [] for i in range(1, N+1)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    ans = 0
    dfs(1, -1)
    
    if S.count('1') == 1 or ans < 1:
        return 0
    elif ans >= 1:
        return ans
    else:
        return -1