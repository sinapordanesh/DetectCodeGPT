def min_time_to_travel(N, M, S, routes, exchanges):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []

    for route in routes:
        U, V, A, B = route
        graph[U].append((V, A, B))
        graph[V].append((U, A, B))

    def dijkstra(start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        visited = [False] * (N+1)
        visited[start] = True
        queue = [start]

        while queue:
            current = queue.pop(0)
            visited[current] = False

            for neighbor, cost, time in graph[current]:
                if distances[current] + time < distances[neighbor]:
                    distances[neighbor] = distances[current] + time
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        return distances

    min_times = []
    for i in range(2, N+1):
        times = dijkstra(1)
        min_times.append(times[i])

    return min_times

# Sample Input
N = 3
M = 2
S = 1
routes = [(1, 2, 1, 2), (1, 3, 2, 4)]
exchanges = [(1, 11), (1, 2)]

print(*min_time_to_travel(N, M, S, routes, exchanges))