def lowest_common_ancestor(N, Q, queries):
    def find_lca(v, w):
        while v != w:
            if v > w:
                v = (v + N - 2) // N
            else:
                w = (w + N - 2) // N
        return v

    result = []
    for query in queries:
        v, w = query
        result.append(find_lca(v, w))
    
    return result

N = 3
Q = 3
queries = [(5, 7), (8, 11), (3, 9)]
print(*lowest_common_ancestor(N, Q, queries))

N = 100000
Q = 2
queries = [(1, 2), (3, 4)]
print(*lowest_common_ancestor(N, Q, queries))