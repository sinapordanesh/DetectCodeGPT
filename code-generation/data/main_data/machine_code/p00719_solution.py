def shortest_time(n, m, p, a, b, horses, roads):
    from collections import defaultdict
    from heapq import heappop, heappush

    graph = defaultdict(list)
    for x, y, z in roads:
        graph[x].append((y, z))
        graph[y].append((x, z))

    for i in range(1, m+1):
        if i != a:
            graph[i].append((i, 0))

    dist = {i: float('inf') for i in range(1, m+1)}
    dist[a] = 0

    pq = [(0, a, horses[:])]
    while pq:
        time, node, tickets = heappop(pq)

        if node == b:
            return round(time, 3)

        if not tickets:
            continue

        for neighbor, edge_time in graph[node]:
            for i, ticket in enumerate(tickets):
                horses_used = ticket
                new_tickets = tickets[:i] + tickets[i+1:]
                new_time = time + edge_time / horses_used
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heappush(pq, (new_time, neighbor, new_tickets))

    return "Impossible"