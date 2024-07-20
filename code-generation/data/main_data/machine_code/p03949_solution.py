def tree_integers(N, edges, K, vertices):
    adj_list = {i: [] for i in range(1, N+1)}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    initial_values = {}
    for i in range(K):
        initial_values[vertices[i][0]] = vertices[i][1]
    
    values = [-1] * (N+1)
    
    stack = [(v, 0) for v in initial_values.keys()]
    while stack:
        node, value = stack.pop()
        if values[node] != -1 and values[node] != value:
            print("No")
            return
        values[node] = value
        for neighbor in adj_list[node]:
            if values[neighbor] == -1:
                stack.append((neighbor, value + 1))
    
    print("Yes")
    for i in range(1, N+1):
        print(values[i])

# Sample Input 1
N = 5
edges = [(1, 2), (3, 1), (4, 3), (3, 5)]
K = 2
vertices = [(2, 6), (5, 7)]
tree_integers(N, edges, K, vertices)

# Sample Input 2
N = 5
edges = [(1, 2), (3, 1), (4, 3), (3, 5)]
K = 3
vertices = [(2, 6), (4, 3), (5, 7)]
tree_integers(N, edges, K, vertices)

# Sample Input 3
N = 4
edges = [(1, 2), (2, 3), (3, 4)]
K = 1
vertices = [(1, 0)]
tree_integers(N, edges, K, vertices)