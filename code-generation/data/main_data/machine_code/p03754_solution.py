def degree_of_vertices(n, edges):
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    for vertex in graph:
        print(len(graph[vertex]))

degree_of_vertices(4, [(1, 2), (2, 4), (4, 3)])