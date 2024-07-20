def longest_path(input):
    # Parse the input
    graphs = []
    current_graph = []
    for line in input:
        if line == "0 0":
            graphs.append(current_graph)
            current_graph = []
        else:
            current_graph.append(list(map(int, line.split())))

    # Define a helper function to find the longest path starting from a given station
    def dfs(graph, current_station, visited, current_path, current_distance):
        visited[current_station] = True
        current_path.append(current_station)
        longest_path = (current_distance, current_path.copy())

        for edge in graph:
            if current_station in edge[:2]:
                next_station = edge[1] if edge[0] == current_station else edge[0]
                if not visited[next_station]:
                    path_distance, path = dfs(graph, next_station, visited, current_path, current_distance + edge[2])
                    if path_distance > longest_path[0]:
                        longest_path = (path_distance, path)
        
        current_path.pop()
        visited[current_station] = False
        return longest_path

    # Find the longest path for each graph
    result = ""
    for graph in graphs:
        stations = set([edge[0] for edge in graph] + [edge[1] for edge in graph])
        longest_path_length = 0
        longest_path_stations = []
        
        for station in stations:
            visited = {station: False for station in stations}
            path_distance, path = dfs(graph, station, visited, [], 0)
            if path_distance > longest_path_length:
                longest_path_length = path_distance
                longest_path_stations = path
        
        result += f"{longest_path_length}\n{' '.join(map(str, longest_path_stations))}\n"

    return result

# Sample Input
input = [
    "6 5",
    "1 3 10",
    "2 3 12",
    "3 4 2",
    "4 5 13",
    "4 6 11",
    "10 10",
    "1 2 11",
    "2 3 25",
    "2 5 81",
    "2 6 82",
    "4 5 58",
    "5 9 68",
    "6 7 80",
    "6 9 67",
    "8 9 44",
    "9 10 21",
    "0 0"
]

print(longest_path(input))