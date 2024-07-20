def height_of_tree(n, edges):
    tree = {}
    for i in range(n):
        tree[i] = []
    
    for edge in edges:
        tree[edge[0]].append((edge[1], edge[2]))
        tree[edge[1]].append((edge[0], edge[2]))
    
    def dfs(node, parent):
        max_height = 0
        for neighbor, weight in tree[node]:
            if neighbor != parent:
                max_height = max(max_height, weight + dfs(neighbor, node))
        
        return max_height
    
    heights = []
    for i in range(n):
        height = dfs(i, -1)
        heights.append(height)
    
    return heights

# Sample Input
n = 4
edges = [(0, 1, 2), (1, 2, 1), (1, 3, 3)]
print(height_of_tree(n, edges))