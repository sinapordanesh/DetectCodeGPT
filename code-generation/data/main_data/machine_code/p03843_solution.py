def possible_combinations(N, edges, s):
    adj_list = {}
    for i in range(N-1):
        a, b = edges[i]
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def dfs(node, parent, black):
        if s[node-1] == '1':
            black = min(black+1, N)
        res = 1 if black > 0 else 0
        for neighbor in adj_list[node]:
            if neighbor != parent:
                res *= dfs(neighbor, node, black)
        return res
    
    return dfs(1, -1, 0) * 2

# Sample Input 1
print(possible_combinations(4, [(1, 2), (1, 3), (1, 4)], "1100"))

# Sample Input 2
print(possible_combinations(5, [(1, 2), (1, 3), (1, 4), (4, 5)], "11111"))

# Sample Input 3
print(possible_combinations(6, [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6)], "100011"))