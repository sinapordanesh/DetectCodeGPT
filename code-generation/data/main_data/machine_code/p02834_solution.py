def aoki_moves(N, u, v, edges):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    for edge in edges:
        a, b = edge
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def dfs(node, parent):
        if node == u:
            return [0, 0]
        if node == v:
            return [1, 0]
        
        res = [0, float('inf')]
        for neighbor in adj_list[node]:
            if neighbor != parent:
                temp = dfs(neighbor, node)
                res[0] += temp[0]
                res[1] = min(res[1], temp[1] + 1)
        
        return res
    
    result = dfs(v, -1)
    return result[1] - 1

# Sample Input 1
print(aoki_moves(5, 4, 1, [(1, 2), (2, 3), (3, 4), (3, 5)]))

# Sample Input 2
print(aoki_moves(5, 4, 5, [(1, 2), (1, 3), (1, 4), (1, 5)]))

# Sample Input 3
print(aoki_moves(2, 1, 2, [(1, 2)]))

# Sample Input 4
print(aoki_moves(9, 6, 1, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (4, 7), (7, 8), (8, 9)]))