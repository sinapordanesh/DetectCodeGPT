def sibling_rivalry(n, m, a, b, c, arrows):
    adj_list = {i: [] for i in range(1, n+1)}
    for u, v in arrows:
        adj_list[u].append(v)
    
    def dfs(node, steps):
        if node == n:
            return steps == 0
        if steps == 0:
            return False
        
        for neighbor in adj_list[node]:
            if dfs(neighbor, (steps - 1) % a) or dfs(neighbor, (steps - 1) % b) or dfs(neighbor, (steps - 1) % c):
                return True
        return False
    
    if dfs(1, a) or dfs(1, b) or dfs(1, c):
        return 1
    
    for neighbor in adj_list[1]:
        if dfs(neighbor, (a - 1) % a) or dfs(neighbor, (a - 1) % b) or dfs(neighbor, (a - 1) % c):
            return 2
    
    return "IMPOSSIBLE"