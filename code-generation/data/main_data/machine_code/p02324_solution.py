def chinese_postman_problem(vertices, edges):
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append((edge[1], edge[2]))
        graph[edge[1]].append((edge[0], edge[2]))

    odd_vertices = [v for v in graph if len(graph[v]) % 2 != 0]

    def min_distance(u, visited, total):
        if len(visited) == len(graph) and u in odd_vertices:
            return total
        elif len(visited) == len(graph):
            return total - graph[u][visited[-1]][1]

        min_dist = float('inf')
        for v in graph[u]:
            if v[0] not in visited:
                new_visited = visited.copy()
                new_visited.append(v[0])
                new_total = total + v[1]
                min_dist = min(min_dist, min_distance(v[0], new_visited, new_total))
        
        return min_dist

    start_vertex = list(graph.keys())[0]
    return min_distance(start_vertex, [start_vertex], 0)