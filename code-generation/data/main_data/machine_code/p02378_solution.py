def bipartite_matching(X, Y, edges):
    graph = {}
    for i in range(X):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])

    match = [-1] * Y
    result = 0
    for i in range(X):
        visited = [False] * X
        if find_match(i, graph, match, visited):
            result += 1
    return result

def find_match(u, graph, match, visited):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if match[v] == -1 or find_match(match[v], graph, match, visited):
                match[v] = u
                return True
    return False

# Sample Input
X = 3
Y = 4
edges = [(0, 0), (0, 2), (0, 3), (1, 1), (2, 1), (2, 3)]
print(bipartite_matching(X, Y, edges))