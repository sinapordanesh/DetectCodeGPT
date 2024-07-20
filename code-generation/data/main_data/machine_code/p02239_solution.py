def bfs_shortest_distance(n, graph):
    distances = [-1] * n
    distances[0] = 0
    queue = [1]
    
    while queue:
        current_node = queue.pop(0)
        for neighbor in graph[current_node]:
            if distances[neighbor-1] == -1:
                distances[neighbor-1] = distances[current_node-1] + 1
                queue.append(neighbor)
    
    for i in range(n):
        print(f"{i+1} {distances[i]}")

n = int(input())
graph = {}
for i in range(n):
    line = input().split()
    node = int(line[0])
    neighbors = [int(x) for x in line[2:]]
    graph[node] = neighbors

bfs_shortest_distance(n, graph)