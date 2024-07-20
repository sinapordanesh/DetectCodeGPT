def distance_on_tree(N, Q, edges, queries):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    
    for edge in edges:
        a, b, c, d = edge
        adj_list[a].append((b, c, d))
        adj_list[b].append((a, c, d))
    
    colors = {}
    for i in range(Q):
        x, y, u, v = queries[i]
        colors[x] = y
        ans = 0
        visited = [False] * (N+1)
        queue = [(u, 0)]
        
        while queue:
            node, dist = queue.pop(0)
            visited[node] = True
            if node == v:
                ans = dist
                break
            for neighbor, color, length in adj_list[node]:
                if color == x and not visited[neighbor]:
                    queue.append((neighbor, dist + colors[x]))
                elif not visited[neighbor]:
                    queue.append((neighbor, dist + length))
        
        print(ans)