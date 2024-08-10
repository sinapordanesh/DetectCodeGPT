def range_query_on_tree(n, nodes, queries):
    tree = {}
    for node in nodes:
        tree[node[1]] = node[2:]
    
    weights = [0] * n
    
    def add(v, w):
        weights[v] += w
    
    def getSum(u):
        total = weights[0]
        while u != 0:
            total += weights[u]
            u = nodes[u-1][0]
        return total
    
    result = []
    for query in queries:
        if query[0] == 0:
            add(query[1], query[2])
        elif query[0] == 1:
            result.append(getSum(query[1]))
    
    return result