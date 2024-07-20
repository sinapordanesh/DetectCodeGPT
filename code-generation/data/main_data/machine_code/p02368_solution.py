def findStronglyConnectedComponents(V, E, edges, queries):
    graph = {i: [] for i in range(V)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    def dfs(node, visited, stack):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(node)
    
    def transposeGraph():
        transposed = {i: [] for i in range(V)}
        for i in range(V):
            for neighbor in graph[i]:
                transposed[neighbor].append(i)
        return transposed
    
    def dfsUtil(node, visited, result):
        visited[node] = True
        result.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfsUtil(neighbor, visited, result)
        return result
    
    visited = [False] * V
    stack = []
    for i in range(V):
        if not visited[i]:
            dfs(i, visited, stack)
    
    transposed = transposeGraph()
    visited = [False] * V
    result = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            result.append(dfsUtil(node, visited, []))
    
    strong_components = set()
    for component in result:
        strong_components.add(tuple(component))
    
    output = []
    for query in queries:
        u, v = query
        u_component = None
        v_component = None
        for component in strong_components:
            if u in component:
                u_component = component
            if v in component:
                v_component = component
            if u_component and v_component:
                break
        if u_component == v_component:
            output.append(1)
        else:
            output.append(0)
    
    return output

# Sample Input
V = 5
E = 6
edges = [[0, 1], [1, 0], [1, 2], [2, 4], [4, 3], [3, 2]]
queries = [[0, 1], [0, 3], [2, 3], [3, 4]]
print(findStronglyConnectedComponents(V, E, edges, queries))