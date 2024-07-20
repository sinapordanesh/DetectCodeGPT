def single_source_shortest_path(n, graph):
    dist = [float('inf')] * n
    dist[0] = 0

    for u in range(n):
        for i in range(1, len(graph[u]), 2):
            v = graph[u][i - 1]
            weight = graph[u][i]

            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight

    for i in range(n):
        print(i, dist[i])

# Sample input
n = 5
graph = {
    0: [2, 3, 3, 1, 1, 2],
    1: [0, 2, 3, 4],
    2: [0, 3, 3, 1, 4, 1],
    3: [2, 1, 0, 1, 1, 4, 4, 3],
    4: [2, 1, 3, 3]
}

single_source_shortest_path(n, graph)