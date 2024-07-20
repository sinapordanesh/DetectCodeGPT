def topological_sort(vertices, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    in_degree = [0] * vertices
    result = []

    for edge in edges:
        start, end = edge
        graph[start].append(end)
        in_degree[end] += 1

    queue = [i for i in range(vertices) if in_degree[i] == 0]

    while queue:
        node = queue.pop(0)
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

# Sample Input
vertices = 6
edges = [(0, 1), (1, 2), (3, 1), (3, 4), (4, 5), (5, 2)]

result = topological_sort(vertices, edges)
for vertex in result:
    print(vertex)