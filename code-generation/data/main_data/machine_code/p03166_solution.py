def longest_directed_path(N, M, edges):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    for edge in edges:
        x, y = edge
        graph[x].append(y)
    
    def dfs(node):
        if node not in graph:
            return 0
        max_length = 0
        for neighbor in graph[node]:
            length = 1 + dfs(neighbor)
            max_length = max(max_length, length)
        return max_length
    
    longest_path = 0
    for i in range(1, N+1):
        longest_path = max(longest_path, dfs(i))
    
    return longest_path

# Input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Output
print(longest_directed_path(N, M, edges))