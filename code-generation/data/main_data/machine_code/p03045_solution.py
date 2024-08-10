def min_cost_to_determine_cards(N, M, queries):
    even_dict = {}
    for i in range(1, N+1):
        even_dict[i] = []
    
    for query in queries:
        X, Y, Z = query
        even_dict[X].append((Y, Z))
        even_dict[Y].append((X, Z))
    
    visited = [False] * (N+1)
    cost = 0
    
    for i in range(1, N+1):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            while stack:
                curr = stack.pop()
                for j, z in even_dict[curr]:
                    if not visited[j]:
                        visited[j] = True
                        stack.append(j)
            cost += 1
    
    return N - cost
