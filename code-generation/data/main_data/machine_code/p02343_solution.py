def disjoint_set(n, queries):
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def unite(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def same(x, y):
        return 1 if find(x) == find(y) else 0
    
    result = []
    for query in queries:
        com, x, y = query
        if com == 0:
            unite(x, y)
        else:
            result.append(same(x, y))
    
    return result

n = 5
queries = [
    [0, 1, 4],
    [0, 2, 3],
    [1, 1, 2],
    [1, 3, 4],
    [1, 1, 4],
    [1, 3, 2],
    [0, 1, 3],
    [1, 2, 4],
    [1, 3, 0],
    [0, 0, 4],
    [1, 0, 2],
    [1, 3, 0]
]

disjoint_set(n, queries)