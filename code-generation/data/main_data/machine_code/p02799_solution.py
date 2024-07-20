def color_assignment(N, M, D, edges):
    adj_list = {i: [] for i in range(1, N+1)}
    for edge in edges:
        adj_list[edge[0]].append(edge)
        adj_list[edge[1]].append(edge)
    
    colors = ['W'] * N
    weights = []
    
    for i in range(1, N+1):
        if len(adj_list[i]) == 1:
            if colors[i-1] == 'W':
                colors[adj_list[i][0][1]-1] = 'B'
            else:
                colors[adj_list[i][0][0]-1] = 'B'
            weights.append(D[i-1])
    
    for i in range(1, N+1):
        if colors[i-1] == 'W':
            for edge in adj_list[i]:
                if colors[edge[0]-1] == 'B' or colors[edge[1]-1] == 'B':
                    weights.append(D[i-1])
                    break
    
    if len(weights) != M:
        print(-1)
        return
    
    print(''.join(colors))
    for weight in weights:
        print(weight)