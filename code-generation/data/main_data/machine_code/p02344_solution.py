def weighted_union_find_trees(n, queries):
    parent = list(range(n))
    weight = [0] * n

    def find(x):
        nonlocal parent, weight
        if parent[x] == x:
            return x
        p = find(parent[x])
        weight[x] += weight[parent[x]]
        parent[x] = p
        return p

    def union(x, y, diff):
        nonlocal parent, weight
        px = find(x)
        py = find(y)
        if px == py:
            return
        parent[py] = px
        weight[py] = weight[x] - weight[y] + diff

    result = []
    for q in queries:
        if q[0] == 0:
            union(q[1], q[2], q[3])
        else:
            if find(q[1]) != find(q[2]):
                result.append("?")
            else:
                result.append(weight[q[1]] - weight[q[2]])
    
    return result

# Sample Input
n = 5
queries = [
    [0, 0, 2, 5],
    [0, 1, 2, 3],
    [1, 0, 1],
    [1, 1, 3],
    [0, 1, 4, 8],
    [1, 0, 4]
]

print(weighted_union_find_trees(n, queries))