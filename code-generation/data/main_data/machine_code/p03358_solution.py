def min_seconds(N, edges, colors):
    adj_list = {i: [] for i in range(1, N+1)}
    for x, y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    white = sum(1 for c in colors if c == 'W')
    
    def dfs(node, parent):
        white_count = 0
        black_count = 0
        for neighbor in adj_list[node]:
            if neighbor == parent:
                continue
            w, b = dfs(neighbor, node)
            white_count += w
            black_count += b
        
        if colors[node-1] == 'W':
            white_count += 1
        
        if white_count == 0 or white_count == white:
            return white_count, black_count
        return white_count, black_count + 2
    
    return dfs(1, 0)[1] - 1

# Sample Input 1
print(min_seconds(5, [(1, 2), (2, 3), (2, 4), (4, 5)], 'WBBWW')) # Output: 5

# Sample Input 2
print(min_seconds(6, [(3, 1), (4, 5), (2, 6), (6, 1), (3, 4)], 'WWBWBB')) # Output: 7

# Sample Input 3
print(min_seconds(1, [], 'B')) # Output: 0

# Sample Input 4
print(min_seconds(20, [(2, 19), (5, 13), (6, 4), (15, 6), (12, 19), (13, 19), (3, 11), (8, 3), (3, 20), (16, 13), (7, 14), (3, 17), (7, 8), (10, 20), (11, 9), (8, 18), (8, 2), (10, 1), (6, 13)], 'WBWBWBBWWWBBWWBBBBBW')) # Output: 21