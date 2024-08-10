def marked_ancestor(N, Q, nodes, queries):
    marked = {1}
    sum_output = 0
    
    for query in queries:
        if query[0] == 'M':
            marked.add(int(query[2]))
        else:
            v = int(query[2])
            ancestor = nodes[v-1]
            while ancestor not in marked:
                ancestor = nodes[ancestor-1]
            sum_output += ancestor
    
    return sum_output

print(marked_ancestor(6, 3, [1, 1, 2, 3, 3], ['Q 5', 'M 3', 'Q 5']))