def squid_painting(N, M, edges, Q, operations):
    colors = [0] * N
    graph = {i: set() for i in range(1, N+1)}
    
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    
    for v, d, c in operations:
        queue = [(v, 0)]
        visited = set()
        
        while queue:
            node, dist = queue.pop(0)
            if dist > d:
                break
            if node not in visited:
                colors[node-1] = c
                visited.add(node)
                for neighbor in graph[node]:
                    queue.append((neighbor, dist+1))
    
    return colors

# Sample Input 1
N = 7
M = 7
edges = [(1, 2), (1, 3), (1, 4), (4, 5), (5, 6), (5, 7), (2, 3)]
Q = 2
operations = [(6, 1, 1), (1, 2, 2)]
print(*squid_painting(N, M, edges, Q, operations))

# Sample Input 2
N = 14
M = 10
edges = [(1, 4), (5, 7), (7, 11), (4, 10), (14, 7), (14, 3), (6, 14), (8, 11), (5, 13), (8, 3)]
Q = 8
operations = [(8, 6, 2), (9, 7, 85), (6, 9, 3), (6, 7, 5), (10, 3, 1), (12, 9, 4), (9, 6, 6), (8, 2, 3)]
print(*squid_painting(N, M, edges, Q, operations))