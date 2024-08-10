def min_edges_to_remove(N, M, X, edges):
    parent = list(range(N+1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    edges.sort(key=lambda x: x[2])
    
    components_weight = [0] * (N+1)
    removed_edges = 0
    
    for i in range(M):
        A, B, Y = edges[i]
        if find(A) != find(B):
            if components_weight[find(A)] + components_weight[find(B)] >= Y:
                union(A, B)
                components_weight[find(A)] = max(components_weight[find(A)], components_weight[find(B)])
            else:
                removed_edges += 1
    
    return removed_edges

# Sample Input 1
N = 4
M = 4
X = [2, 3, 5, 7]
edges = [(1, 2, 7), (1, 3, 9), (2, 3, 12), (3, 4, 18)]
print(min_edges_to_remove(N, M, X, edges))

# Sample Input 2
N = 6
M = 10
X = [4, 4, 1, 1, 1, 7]
edges = [(3, 5, 19), (2, 5, 20), (4, 5, 8), (1, 6, 16), (2, 3, 9), (3, 6, 16), (3, 4, 1), (2, 6, 20), (2, 4, 19), (1, 2, 9)]
print(min_edges_to_remove(N, M, X, edges))

# Sample Input 3
N = 10
M = 9
X = [81, 16, 73, 7, 2, 61, 86, 38, 90, 28]
edges = [(6, 8, 725), (3, 10, 12), (1, 4, 558), (4, 9, 615), (5, 6, 942), (8, 9, 918), (2, 7, 720), (4, 7, 292), (7, 10, 414)]
print(min_edges_to_remove(N, M, X, edges))