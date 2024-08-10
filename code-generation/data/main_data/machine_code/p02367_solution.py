def find_bridges(n, edges):
    def dfs(node, parent, visited, disc, low, bridges):
        nonlocal time
        visited[node] = True
        disc[node] = time
        low[node] = time
        time += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, node, visited, disc, low, bridges)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:
                    bridges.append((min(node, neighbor), max(node, neighbor)))
            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])
    
    graph = {i: [] for i in range(n)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    visited = [False] * n
    disc = [-1] * n
    low = [-1] * n
    time = 0
    bridges = []
    
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, visited, disc, low, bridges)
    
    return sorted(bridges)


# Sample Input
n = 4
edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
print(find_bridges(n, edges))

n = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(find_bridges(n, edges))