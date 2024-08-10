def range_query_on_tree_II(n, nodes, queries):
    tree = {}
    for i in range(n):
        k, *children = nodes[i]
        tree[i] = (k, children)
        
    def add(v, w):
        nonlocal tree
        stack = [(0, 0)]  # (node, weight)
        while stack:
            node, weight = stack.pop()
            k, children = tree[node]
            tree[node] = (k, children)
            for child in children:
                stack.append((child, weight + w))
    
    def getSum(u):
        nonlocal tree
        total_sum = 0
        stack = [(0, 0)]  # (node, weight)
        while stack:
            node, weight = stack.pop()
            k, children = tree[node]
            total_sum += weight
            for child in children:
                stack.append((child, weight))
            if node == u:
                break
        return total_sum
    
    result = []
    for query in queries:
        if query[0] == 0:
            add(query[1], query[2])
        elif query[0] == 1:
            result.append(getSum(query[1]))
    
    return result