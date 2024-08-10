def max_restaurants(datasets):
    results = []
    for data in datasets:
        n, m, l, s, t = data[0]
        restaurants = data[1]
        
        graph = {}
        for i in range(1, n+1):
            graph[i] = []
        
        for i in range(m):
            a, b, c = data[2][i]
            graph[a].append((b, c))
            graph[b].append((a, c))
            
        siro_locations = {}
        for i in range(l):
            j, e = data[3][i]
            siro_locations[j] = e
        
        visited = [False] * (n+1)
        time = 0
        num_restaurants = 0
        
        def dfs(node):
            nonlocal time, num_restaurants
            visited[node] = True
            if node in siro_locations and time + siro_locations[node] <= t:
                num_restaurants += 1
                time += siro_locations[node]
            
            for neighbor, c in graph[node]:
                if time + c * 2 <= t and not visited[neighbor]:
                    time += c
                    dfs(neighbor)
                    time += c
        
        dfs(s)
        results.append(num_restaurants)
    
    return results

# Sample Input Parsing
datasets = [
    ((2, 1, 1, 1, 10), [(1, 2, 3)], [(2, 4)]),
    ((2, 1, 1, 1, 9), [(1, 2, 3)], [(2, 4)]),
    ((4, 2, 2, 4, 50), [(1, 2, 5), (3, 4, 5)], [(2, 15), (3, 15)]),
    ((4, 6, 3, 1, 29), [(1, 2, 20), (3, 2, 10), (4, 1, 5), (3, 1, 5), (2, 4, 3), (3, 4, 4)], [(2, 1), (4, 5), (3, 3)])
]

# Function Call
print(max_restaurants(datasets))