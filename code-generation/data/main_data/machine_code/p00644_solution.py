def winter_bells(n, m, p, edges, children):
    def shortest_paths(graph, start, end):
        queue = [(start, [start])]
        while queue:
            (node, path) = queue.pop(0)
            for next_node in graph[node]:
                if next_node in path:
                    continue
                if next_node == end:
                    yield path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))
    
    def calculate_probability(graph, start, end):
        total_paths = list(shortest_paths(graph, start, end))
        total_weight = sum(len(path)-1 for path in total_paths)
        probabilities = {node: 0 for node in graph}
        for path in total_paths:
            for node in path[1:]:
                probabilities[node] += 1 / len(total_paths)
        return probabilities
    
    graph = {i: {} for i in range(n)}
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    
    result = []
    for child in children:
        probabilities = calculate_probability(graph, 0, child)
        result.append(probabilities[child])
    
    return result

# Sample Input
n = 3
m = 2
p = 1
edges = [(0, 1, 2), (1, 2, 3)]
children = [1]
print(winter_bells(n, m, p, edges, children))

n = 4
m = 5
p = 2
edges = [(0, 1, 1), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 3, 1)]
children = [1, 2]
print(winter_bells(n, m, p, edges, children) )