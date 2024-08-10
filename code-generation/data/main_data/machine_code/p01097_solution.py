def minimal_surface_area(n, k, s, positions):
    if k == 1:
        return 6 * s * s
    
    if n < k:
        return -1
    
    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
    
    def can_connect(p1, p2):
        return distance(p1, p2) <= 2 * s
    
    def dfs(node, visited, connections):
        visited.add(node)
        for neighbor in range(n):
            if neighbor not in visited and can_connect(positions[node], positions[neighbor]):
                connections.add(node)
                dfs(neighbor, visited, connections)
    
    all_connections = []
    for i in range(n):
        visited = set()
        connections = set()
        dfs(i, visited, connections)
        all_connections.append(connections)
    
    for i in range(n):
        if len(all_connections[i]) >= k - 1:
            surface_area = 6 * k * s * s
            return surface_area
    
    return -1

# Sample Input
print(minimal_surface_area(1, 1, 100, [[100, 100, 100]]))
print(minimal_surface_area(6, 4, 10, [[100, 100, 100], [106, 102, 102], [112, 110, 104], [104, 116, 102], [100, 114, 104], [92, 107, 100]]))
print(minimal_surface_area(10, 4, 10, [[-100, 101, 100], [-108, 102, 120], [-116, 103, 100], [-124, 100, 100], [-132, 99, 100], [-92, 98, 100], [-84, 100, 140], [-76, 103, 100], [-68, 102, 100], [-60, 101, 100]]))