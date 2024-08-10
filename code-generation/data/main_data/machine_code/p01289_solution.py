def strange_couple(n, s, t, signs, distances):
    while True:
        if n == 0:
            break
        n -= 1
        if signs[n] == 0:
            signs[n] = [i for i in range(n)]
        else:
            signs[n] = [n]
            
    dist = [float('inf')] * n
    dist[s-1] = 0
    q = [s-1]
    
    while q:
        u = q.pop(0)
        for v in range(n):
            if distances[u][v] != 0 and dist[v] > dist[u] + distances[u][v]:
                dist[v] = dist[u] + distances[u][v]
                q.append(v)
    
    if dist[t-1] == float('inf'):
        return "impossible"
    return round(dist[t-1], 8)