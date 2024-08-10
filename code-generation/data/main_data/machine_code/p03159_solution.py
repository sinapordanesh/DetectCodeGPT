def disable_server(N, arr, cables):
    adj_list = {i: [] for i in range(1, N+1)}
    for u, v in cables:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    total_power = sum([abs(power) for power in arr])
    
    def dfs(node, parent):
        nonlocal total_power
        power = arr[node-1]
        for neighbor in adj_list[node]:
            if neighbor != parent:
                power += dfs(neighbor, node)
        if power < 0:
            total_power -= abs(arr[node-1])
            return 0
        return power
    
    dfs(1, 0)
    
    return len(adj_list) - 1 if total_power < 0 else 0