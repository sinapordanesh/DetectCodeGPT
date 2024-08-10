
def find_min_vertices_to_remove(N, K, edges):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    def diameter(node, parent):
        max_depth = 0
        depths = []
        for neighbor in adj_list[node]:
            if neighbor != parent:
                depth = diameter(neighbor, node)
                depths.append(depth)
                max_depth = max(max_depth, depth)
        
        depths.sort(reverse=True)
        if len(depths) >= 2:
            non_leaf_diameters.append(sum(depths[:2]) + 2)
        
        return max_depth + 1
        
    min_vertices_to_remove = float('inf')
    for i in range(1, N+1):
        non_leaf_diameters = []
        diameter(i, -1)
        non_leaf_diameters.sort(reverse=True)
        count = 0
        for diameter in non_leaf_diameters:
            if diameter > K:
                count += 1
            else:
                break
        
        min_vertices_to_remove = min(min_vertices_to_remove, count)
    
    return min_vertices_to_remove

# Input
N, K = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N-1)]

# Output
print(find_min_vertices_to_remove(N, K, edges))