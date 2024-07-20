def city_connections(N, K, L, road_connections, railway_connections):
    road_graph = {i: set() for i in range(1, N+1)}
    railway_graph = {i: set() for i in range(1, N+1)}
    
    for p, q in road_connections:
        road_graph[p].add(q)
        road_graph[q].add(p)
    
    for r, s in railway_connections:
        railway_graph[r].add(s)
        railway_graph[s].add(r)
    
    result = []
    for city in range(1, N+1):
        connected_cities = road_graph[city].intersection(railway_graph[city])
        result.append(len(connected_cities))
    
    return result