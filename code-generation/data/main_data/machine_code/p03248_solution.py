def construct_tree(s):
    n = len(s)
    if s.count('1') == n:
        print(-1)
    else:
        edges = []
        current_node = 1
        for i in range(1, n):
            if s[i] == '1':
                edges.append((current_node, i+1))
            else:
                edges.append((current_node+1, i+1))
                current_node += 1
        for edge in edges:
            print(edge[0], edge[1])