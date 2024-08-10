def max_sequence(N, edges):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    def dfs(node, parent, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node, visited)
    
    visited = set()
    dfs(1, -1, visited)
    
    return len(visited) - 1

# Sample Input 1
N = 4
edges = [(1, 2), (2, 3), (2, 4)]
print(max_sequence(N, edges))

# Sample Input 2
N = 10
edges = [(7, 9), (1, 2), (6, 4), (8, 1), (3, 7), (6, 5), (2, 10), (9, 6), (2, 6)]
print(max_sequence(N, edges))