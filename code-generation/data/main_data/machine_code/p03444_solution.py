def rooted_tree_operations(N, parents, values):
    operations = []
    
    def rotate_values(vertex):
        path = [vertex]
        while vertex != 0:
            vertex = parents[vertex]
            path.append(vertex)
        path.reverse()
        
        for i in range(len(path) - 1):
            values[path[i]], values[path[i+1]] = values[path[i+1]], values[path[i]]
            
        operations.append(path[-1] + 1)
    
    for _ in range(25000):
        if all(values[i] == i for i in range(N)):
            break
        
        for i in range(N):
            if values[i] == i:
                continue
            rotate_values(i)
    
    return len(operations), operations