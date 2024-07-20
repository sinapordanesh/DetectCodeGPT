from collections import defaultdict

def diameter_of_tree(n, edges):
    graph = defaultdict(list)
    
    for edge in edges:
        u, v, w = edge
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    def dfs(node, parent):
        nonlocal diameter
        max_depth = second_max_depth = 0
        
        for neighbor, weight in graph[node]:
            if neighbor == parent:
                continue
            depth = dfs(neighbor, node) + weight
            if depth > max_depth:
                second_max_depth = max_depth
                max_depth = depth
            elif depth > second_max_depth:
                second_max_depth = depth
        
        diameter = max(diameter, max_depth + second_max_depth)
        return max_depth
    
    diameter = 0
    dfs(0, -1)
    
    return diameter

# Sample Input 1
n = 4
edges = [(0, 1, 2), (1, 2, 1), (1, 3, 3)]
print(diameter_of_tree(n, edges))

# Sample Input 2
n = 4
edges = [(0, 1, 1), (1, 2, 2), (2, 3, 4)]
print(diameter_of_tree(n, edges))