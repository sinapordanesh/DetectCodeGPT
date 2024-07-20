def construct_directed_graph(N, M, edges):
    adj_list = {}
    out_degrees = [0] * N
    
    for i in range(1, N+1):
        adj_list[i] = []
    
    for edge in edges:
        a, b = edge
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    for i in range(1, N+1):
        out_degrees[i-1] = len(adj_list[i]) 
    
    if any(deg % 2 != 0 for deg in out_degrees):
        print(-1)
        return
    
    for edge in edges:
        print(f"{edge[0]} {edge[1]}")