def medical_inspection(n, m, k, connections):
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    components = []
    for i in range(1, n+1):
        if i not in visited:
            component = set()
            stack = [i]
            while stack:
                node = stack.pop()
                if node not in component:
                    component.add(node)
                    visited.add(node)
                    stack.extend(graph[node])
            components.append(component)
    
    if len(components) > k:
        return "Impossible"
    return len(components)