def game_end(N, X, Y, red_edges, blue_edges):
    adj_list_red = {i:[] for i in range(1, N+1)}
    adj_list_blue = {i:[] for i in range(1, N+1)}
    
    for edge in red_edges:
        a, b = edge
        adj_list_red[a].append(b)
        adj_list_red[b].append(a)
        
    for edge in blue_edges:
        c, d = edge
        adj_list_blue[c].append(d)
        adj_list_blue[d].append(c)
    
    visited = [False] * (N+1)
    queue = [(X, 0)]
    
    while queue:
        node, dist = queue.pop(0)
        visited[node] = True
        
        if node == Y:
            return dist
        
        for neighbor in adj_list_red[node]:
            if not visited[neighbor]:
                queue.append((neighbor, dist+1))
        
        for neighbor in adj_list_blue[node]:
            if not visited[neighbor]:
                queue.append((neighbor, dist+1))
    
    return -1