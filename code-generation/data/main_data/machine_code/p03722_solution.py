def maximize_score(N, M, edges):
    graph = {i: [] for i in range(1, N+1)}
    for a, b, c in edges:
        graph[a].append((b, c))
    
    dp = [-float('inf')] * (N+1)
    dp[1] = 0
    
    for _ in range(N-1):
        updated = False
        for v in range(1, N+1):
            for u, w in graph[v]:
                if dp[v] + w > dp[u]:
                    dp[u] = dp[v] + w
                    updated = True
        if not updated:
            break
            
    for v in range(1, N+1):
        for u, w in graph[v]:
            if dp[v] + w > dp[u]:
                return "inf"
            
    return dp[N]