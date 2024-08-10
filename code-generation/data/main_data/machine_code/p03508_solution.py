def max_edges_to_add(N, M, edges):
    import collections
    
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        
        if x_root == y_root:
            return False
        
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
        
        return True

    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    count = N - 2

    for a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            count -= 1

    return count

# Sample Input 1
N = 4
M = 1
edges = [(1, 3)]
print(max_edges_to_add(N, M, edges))

# Sample Input 2
N = 2
M = 0
edges = []
print(max_edges_to_add(N, M, edges))

# Sample Input 3
N = 9
M = 6
edges = [(1, 4), (1, 8), (2, 5), (3, 6), (4, 8), (5, 7)]
print(max_edges_to_add(N, M, edges))