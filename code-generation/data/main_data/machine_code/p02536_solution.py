def min_roads_to_build(N, M, roads):
    graph = {i: set() for i in range(1, N+1)}
    for road in roads:
        graph[road[0]].add(road[1])
        graph[road[1]].add(road[0])
    
    components = []
    visited = set()
    
    for city in range(1, N+1):
        if city not in visited:
            component = set()
            stack = [city]
            while stack:
                current_city = stack.pop()
                if current_city not in component:
                    component.add(current_city)
                    visited.add(current_city)
                    stack.extend(graph[current_city])
            components.append(component)
    
    min_roads = 0
    for i in range(len(components)-1):
        min_roads += len(components[i]) * len(components[i+1])
    
    return min_roads

# Sample Input
N = 3
M = 1
roads = [(1, 2)]

print(min_roads_to_build(N, M, roads))