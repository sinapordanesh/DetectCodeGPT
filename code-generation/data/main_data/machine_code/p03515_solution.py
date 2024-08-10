def niceness(N, edges):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    for a, b, c in edges:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    def dfs(node, parent, min_joy):
        total_joy = min_joy
        for neighbor, joy in graph[node]:
            if neighbor != parent:
                total_joy += dfs(neighbor, node, min(min_joy, joy))
        return total_joy
    
    result = []
    for i in range(1, N+1):
        result.append(dfs(i, 0, float('inf')))
    
    return result

# Sample Input 1
print(niceness(3, [(1, 2, 10), (2, 3, 20)]))

# Sample Input 2
print(niceness(15, [(6, 3, 2), (13, 3, 1), (1, 13, 2), (7, 1, 2), (8, 1, 1), (2, 8, 2), (2, 12, 2), (5, 2, 2), (2, 11, 2), (10, 2, 2), (10, 9, 1), (9, 14, 2), (4, 14, 1), (11, 15, 2)]))

# Sample Input 3
print(niceness(19, [(19, 14, 48), (11, 19, 23), (17, 14, 30), (7, 11, 15), (2, 19, 15), (2, 18, 21), (19, 10, 43), (12, 11, 25), (3, 11, 4), (5, 19, 50), (4, 11, 19), (9, 12, 29), (14, 13, 3), (14, 6, 12), (14, 15, 14), (5, 1, 6), (8, 18, 13), (7, 16, 14)]))