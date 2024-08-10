def build_space_station(input_data):
    from math import sqrt
    
    def distance(p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2) - p1[3] - p2[3]
    
    def bellman_ford(graph, start):
        inf = float('inf')
        distances = {node: inf for node in graph}
        distances[start] = 0
        
        for _ in range(len(graph) - 1):
            for node in graph:
                for neighbor in graph[node]:
                    if distances[node] + graph[node][neighbor] < distances[neighbor]:
                        distances[neighbor] = distances[node] + graph[node][neighbor]
        
        return distances
    
    result = []
    while True:
        n = int(input_data.pop(0))
        if n == 0:
            break
        
        cells = [tuple(map(float, input_data.pop(0).split())) for _ in range(n)]
        
        graph = {i: {} for i in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                d = distance(cells[i], cells[j])
                if d < 0:
                    graph[i][j] = -d
                    graph[j][i] = -d
        
        distances = bellman_ford(graph, 0)
        result.append('{:.3f}'.format(sum(distances.values())))
    
    return result

input_data = [
    "3",
    "10.000 10.000 50.000 10.000",
    "40.000 10.000 50.000 10.000",
    "40.000 40.000 50.000 10.000",
    "2",
    "30.000 30.000 30.000 20.000",
    "40.000 40.000 40.000 20.000",
    "5",
    "5.729 15.143 3.996 25.837",
    "6.013 14.372 4.818 10.671",
    "80.115 63.292 84.477 15.120",
    "64.095 80.924 70.029 14.881",
    "39.472 85.116 71.369 5.553",
    "0"
]

print(build_space_station(input_data))