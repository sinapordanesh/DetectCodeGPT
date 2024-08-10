def paint_tree(N, K, edges):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    
    for edge in edges:
        a, b = edge
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def dfs(node, parent, color, colors_used):
        colors_used.add(color)
        
        for neighbor in adj_list[node]:
            if neighbor != parent:
                for new_color in range(1, K+1):
                    if new_color != color:
                        dfs(neighbor, node, new_color, colors_used.copy())
    
    ans = 0
    for i in range(1, K+1):
        dfs(1, -1, i, set())
        ans += len(colors_used)
    
    return ans % 1000000007