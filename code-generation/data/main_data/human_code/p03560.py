from heapq import heappush, heappop


def dijkstra(edge, start, end):
    """
    Create distance(cost) table for all nodes.
    :param edge: List of tuple(to, cost)
    :param start: start node
    :param end: end node
    :return: minimum cost from start to end
    """
    h = [(0, start)]
    used = [False] * len(edge)

    while h:
        cost, node = heappop(h)
        if used[node]:
            continue
        used[node] = True

        if node == end:
            return cost

        for i, c in edge[node]:
            heappush(h, (cost + c, i))

    return -1


K = int(input())

edge = [[] for _ in range(K)]
for i in range(1, K):
    if i % 10 != 9:
        edge[i].append(((i+1) % K, 1))
    edge[i].append(((i*10) % K, 0))

print(dijkstra(edge, 1, 0) + 1)