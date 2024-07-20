import itertools

def is_connected(graph):
    visited = set()
    stack = [next(iter(graph))]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(nei for nei in graph[node] if nei not in visited)
    return len(visited) == len(graph)

def calculate_probability(N, M, P, edges):
    graph = {i: set() for i in range(1, N+1)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    disconnected_count = 0
    for edges_to_remove in itertools.product([True, False], repeat=M):
        temp_graph = {node: set(neighbors) for node, neighbors in graph.items()}
        for i in range(M):
            if edges_to_remove[i]:
                edge = edges[i]
                temp_graph[edge[0]].remove(edge[1])
                temp_graph[edge[1]].remove(edge[0])
        
        if not is_connected(temp_graph):
            disconnected_count += 1

    return 1 - disconnected_count / (2**M)

N, M, P = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
print("{:.12f}".format(calculate_probability(N, M, P, edges)))