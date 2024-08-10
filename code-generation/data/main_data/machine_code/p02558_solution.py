def connected_components(N, Q, queries):
    parent = [i for i in range(N)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    result = []
    
    for query in queries:
        if query[0] == 0:
            union(query[1], query[2])
        else:
            result.append(1 if find(query[1]) == find(query[2]) else 0)
    
    return result

N = 4
Q = 7
queries = [
    [1, 0, 1],
    [0, 0, 1],
    [0, 2, 3],
    [1, 0, 1],
    [1, 1, 2],
    [0, 0, 2],
    [1, 1, 3]
]

print(connected_components(N, Q, queries))