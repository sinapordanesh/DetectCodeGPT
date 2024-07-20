def min_refills(N, M, L, roads, Q, queries):
    def build_graph(roads):
        graph = {}
        for road in roads:
            a, b, c = road
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, c))
            graph[b].append((a, c))
        return graph

    def dijkstra(graph, start, end, tank_capacity):
        pq = [(0, start, tank_capacity)]
        distances = {node: float('inf') for node in graph}
        distances[start] = 0

        while pq:
            cost, node, remaining_fuel = heapq.heappop(pq)
            if node == end:
                return cost

            if remaining_fuel == 0:
                continue

            for neighbor, fuel in graph[node]:
                if cost + fuel < distances[neighbor] and fuel <= remaining_fuel:
                    distances[neighbor] = cost + fuel
                    heapq.heappush(pq, (cost + fuel, neighbor, tank_capacity - fuel))
        return -1

    import heapq
    graph = build_graph(roads)
    result = []
    for query in queries:
        s, t = query
        if s not in graph or t not in graph:
            result.append(-1)
        else:
            result.append(dijkstra(graph, s, t, L))
    return result

# Sample Input 1
N = 3
M = 2
L = 5
roads = [(1, 2, 3), (2, 3, 3)]
Q = 2
queries = [(3, 2), (1, 3)]
print(min_refills(N, M, L, roads, Q, queries))

# Sample Input 2
N = 4
M = 0
L = 1
roads = []
Q = 1
queries = [(2, 1)]
print(min_refills(N, M, L, roads, Q, queries))

# Sample Input 3
N = 5
M = 4
L = 4
roads = [(1, 2, 2), (2, 3, 2), (3, 4, 3), (4, 5, 2)]
Q = 20
queries = [(2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (3, 2), (4, 2), (5, 2), (1, 3), (2, 3), (4, 3), (5, 3), (1, 4), (2, 4), (3, 4), (5, 4), (1, 5), (2, 5), (3, 5), (4, 5)]
print(min_refills(N, M, L, roads, Q, queries))