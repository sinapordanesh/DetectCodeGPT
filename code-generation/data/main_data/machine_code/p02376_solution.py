def max_flow(vertices, edges):
    graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    for edge in edges:
        u, v, c = edge
        graph[u][v] = c
    
    def ford_fulkerson(graph, source, sink):
        def bfs(graph, source, sink, parent):
            visited = [False] * len(graph)
            queue = []
            queue.append(source)
            visited[source] = True
            
            while queue:
                u = queue.pop(0)
                
                for ind, val in enumerate(graph[u]):
                    if visited[ind] == False and val > 0:
                        queue.append(ind)
                        visited[ind] = True
                        parent[ind] = u
                        
            return True if visited[sink] else False
        
        max_flow = 0
        parent = [-1] * len(graph)
        
        while bfs(graph, source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, graph[parent[s]][s])
                s = parent[s]
                
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow
                v = parent[v]
                
        return max_flow
    
    return ford_fulkerson(graph, 0, vertices - 1)