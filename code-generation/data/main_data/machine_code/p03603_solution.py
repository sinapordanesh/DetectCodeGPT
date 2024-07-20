def is_possible(N, P, X):
    adj_list = [[] for _ in range(N+1)]
    for i in range(2, N+1):
        adj_list[P[i-2]].append(i)
    
    def dfs(v):
        white_weight = X[v-1] if adj_list[v] == [] else 0
        black_weight = X[v-1] if adj_list[v] == [] else 0
        
        for child in adj_list[v]:
            if not dfs(child):
                return False
            white_weight = max(white_weight, white_weight + X[child-1])
            black_weight = max(black_weight, black_weight + X[child-1])
        
        if (white_weight < X[v-1] or black_weight < X[v-1] or white_weight + black_weight != 2*X[v-1] or (white_weight - X[v-1]) % 2 != 0):
            return False
        
        return True
    
    return "POSSIBLE" if dfs(1) else "IMPOSSIBLE"