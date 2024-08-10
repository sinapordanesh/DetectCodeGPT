def detect_bug(N, M, rules):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    
    for rule in rules:
        a, b, x = rule
        graph[a].append((b, x))
        graph[b].append((a, x))
    
    visited = [False] * (N+1)
    
    def dfs(node, prev):
        visited[node] = True
        for neighbor, x in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != prev:
                return True
        return False
    
    for i in range(1, N+1):
        if not visited[i]:
            if dfs(i, -1):
                return "No"
    
    return "Yes"

# Test the function with the provided examples
print(detect_bug(4, 4, [(1, 2, 2), (2, 3, 2), (3, 4, 2), (4, 2, 3)]))
print(detect_bug(4, 3, [(1, 2, 7), (2, 3, 5), (4, 1, 2)]))
print(detect_bug(4, 4, [(1, 2, 101), (2, 3, 99), (1, 4, 100), (4, 3, 100)]))
print(detect_bug(5, 6, [(3, 1, 4), (2, 3, 4), (5, 4, 15), (2, 1, 16), (2, 4, 20), (5, 3, 3)]))