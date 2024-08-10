def find_number_of_ways_to_paint(N, M, X, edges):
    mod = 10**9 + 7
    
    def get_parent(parent, x):
        if parent[x] != x:
            parent[x] = get_parent(parent, parent[x])
        return parent[x]
    
    def union(parent, rank, x, y):
        x_root = get_parent(parent, x)
        y_root = get_parent(parent, y)
        
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(N)]
    rank = [0] * N
    black = 0
    white = 0
    
    for u, v, w in edges:
        if get_parent(parent, u) != get_parent(parent, v):
            union(parent, rank, u, v)
            if w < X:
                white += 1
            elif w == X:
                black += 1
    
    return (black * white) % mod

# Sample Input
print(find_number_of_ways_to_paint(3, 3, 2, [(1, 2, 1), (2, 3, 1), (3, 1, 1)])) # 6
print(find_number_of_ways_to_paint(3, 3, 3, [(1, 2, 1), (2, 3, 1), (3, 1, 2)])) # 2
print(find_number_of_ways_to_paint(5, 4, 1, [(1, 2, 3), (1, 3, 3), (2, 4, 6), (2, 5, 8)])) # 0
print(find_number_of_ways_to_paint(8, 10, 49, [(4, 6, 10), (8, 4, 11), (5, 8, 9), (1, 8, 10), (3, 8, 128773450), (7, 8, 10), (4, 2, 4), (3, 4, 1), (3, 1, 13), (5, 2, 2)])) # 4