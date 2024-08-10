def connected_cities(N, K, L, roads, railways):
    road_connections = [0] * N
    railway_connections = [0] * N
    
    graph_roads = [[] for _ in range(N)]
    graph_railways = [[] for _ in range(N)]
    
    for road in roads:
        p, q = road
        graph_roads[p-1].append(q-1)
        graph_roads[q-1].append(p-1)
    
    for railway in railways:
        r, s = railway
        graph_railways[r-1].append(s-1)
        graph_railways[s-1].append(r-1)
    
    def dfs(city, graph, visited):
        visited[city] = True
        for neighbor in graph[city]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited)
    
    for city in range(N):
        visited_roads = [False] * N
        dfs(city, graph_roads, visited_roads)
        for i in range(N):
            if visited_roads[i]:
                road_connections[city] += 1
        
        visited_railways = [False] * N
        dfs(city, graph_railways, visited_railways)
        for i in range(N):
            if visited_railways[i]:
                railway_connections[city] += 1
    
    return road_connections, railway_connections

# Sample input
N = 4
K = 3
L = 1
roads = [(1, 2), (2, 3), (3, 4)]
railways = [(2, 3)]

print(*connected_cities(N, K, L, roads, railways))