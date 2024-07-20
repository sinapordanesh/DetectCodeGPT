def min_total_cost_to_connect_forest(N, M, values, edges):
    parent = [-1] * N
    rank = [0] * N
    
    def find(x):
        if parent[x] == -1:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
    
    edges.sort(key=lambda x: values[x[0]] + values[x[1]], reverse=True)
    
    total_cost = 0
    components = N
    for edge in edges:
        x, y = edge
        if find(x) != find(y):
            union(x, y)
            total_cost += values[x] + values[y]
            components -= 1
            if components == 1:
                break
    
    if components == 1:
        return total_cost
    else:
        return "Impossible"