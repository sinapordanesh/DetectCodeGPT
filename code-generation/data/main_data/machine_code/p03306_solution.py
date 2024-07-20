def find_number_of_ways(n, m, edges):
    def dfs(node, val):
        if visited[node]:
            return val == values[node]
        visited[node] = True
        values[node] = val
        for neighbor, cost in graph[node]:
            if not dfs(neighbor, val - cost):
                return False
        return True

    graph = [[] for _ in range(n)]
    for u, v, s in edges:
        u -= 1
        v -= 1
        graph[u].append((v, s))
        graph[v].append((u, s))

    visited = [False] * n
    values = [0] * n
    for i in range(n):
        if not visited[i]:
            if not dfs(i, 10**9):
                return 0
    return 1

n, m = 3, 3
edges = [(1, 2, 3), (2, 3, 5), (1, 3, 4)]
print(find_number_of_ways(n, m, edges))

n, m = 4, 3
edges = [(1, 2, 6), (2, 3, 7), (3, 4, 5)]
print(find_number_of_ways(n, m, edges))

n, m = 8, 7
edges = [(1, 2, 1000000000), (2, 3, 2), (3, 4, 1000000000), (4, 5, 2), (5, 6, 1000000000), (6, 7, 2), (7, 8, 1000000000)]
print(find_number_of_ways(n, m, edges))