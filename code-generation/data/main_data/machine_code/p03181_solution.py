def ways_to_paint(N, M, edges):
    adj_list = [[] for _ in range(N)]
    for x, y in edges:
        adj_list[x-1].append(y-1)
        adj_list[y-1].append(x-1)
    
    colors = [0] * N
    colors[0] = 1
    
    def dfs(node, parent):
        total_ways = 1
        for neighbor in adj_list[node]:
            if neighbor != parent:
                total_ways *= dfs(neighbor, node) + 1
                total_ways %= M
        colors[node] = total_ways
        return total_ways
    
    dfs(0, -1)
    
    for c in colors:
        print(c)

# Sample Input 1
N = 3
M = 100
edges = [(1, 2), (2, 3)]
ways_to_paint(N, M, edges)

# Sample Input 2
N = 4
M = 100
edges = [(1, 2), (1, 3), (1, 4)]
ways_to_paint(N, M, edges)

# Sample Input 3
N = 1
M = 100
edges = []
ways_to_paint(N, M, edges)

# Sample Input 4
N = 10
M = 2
edges = [(8, 5), (10, 8), (6, 5), (1, 5), (4, 8), (2, 10), (3, 6), (9, 2), (1, 7)]
ways_to_paint(N, M, edges)