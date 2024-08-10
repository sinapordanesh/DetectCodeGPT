def restore_original_rooted_tree(N, M, edges):
    tree = {}
    for i in range(1, N+1):
        tree[i] = []
    
    for edge in edges:
        u, v = edge
        tree[v].append(u)
    
    parents = [0] * (N+1)
    parents[1] = 0
    queue = [1]
    
    while queue:
        node = queue.pop(0)
        for parent in tree[node]:
            if parents[parent] == 0:
                parents[parent] = node
                queue.append(parent)
    
    for i in range(1, N+1):
        print(parents[i])