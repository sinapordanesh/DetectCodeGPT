def connected_components(N, M, edges):
    parent = [i for i in range(N*N)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        parent[root_x] = root_y
    
    for a, b in edges:
        union(a*N+b, b*N+a)
        
    components = set()
    for i in range(N):
        for j in range(N):
            components.add(find(i*N+j))
    
    return len(components)