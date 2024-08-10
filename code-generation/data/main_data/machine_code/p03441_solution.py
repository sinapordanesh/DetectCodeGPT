def min_antennas(N, edges):
    adj_list = {}
    for i in range(N):
        adj_list[i] = []
    
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    def dfs(node, parent, depths, depth):
        depths[node] = depth
        for neighbor in adj_list[node]:
            if neighbor != parent:
                dfs(neighbor, node, depths, depth + 1)
    
    depths = [0] * N
    dfs(0, -1, depths, 0)
    
    max_depth = max(depths)
    farthest_nodes = [i for i in range(N) if depths[i] == max_depth]
    
    ant_needed = max_depth // 2 + max_depth % 2
    return max(ant_needed, len(farthest_nodes))

# Sample Input 1
print(min_antennas(5, [(0, 1), (0, 2), (0, 3), (3, 4)]))
# Sample Input 2
print(min_antennas(2, [(0, 1)]))
# Sample Input 3
print(min_antennas(10, [(2, 8), (6, 0), (4, 1), (7, 6), (2, 3), (8, 6), (6, 9), (2, 4), (5, 8)]))