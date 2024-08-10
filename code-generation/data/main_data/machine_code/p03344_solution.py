def smallest_initial_amount_of_money(N, M, values, edges):
    def dfs(node, parent):
        total_needed = values[node]
        for neighbor in edges[node]:
            if neighbor == parent:
                continue
            total_needed += dfs(neighbor, node)
        return max(total_needed, values[node])
    
    graph = {i: [] for i in range(1, N+1)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    return dfs(1, -1)

# Sample Input 1
N = 4
M = 5
values = [3, 1, 4, 6]
edges = [(1, 2), (2, 3), (2, 4), (1, 4), (3, 4)]
print(smallest_initial_amount_of_money(N, M, values, edges))

# Sample Input 2
N = 5
M = 8
values = [6, 15, 15, 15, 20]
edges = [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)]
print(smallest_initial_amount_of_money(N, M, values, edges))

# Sample Input 3
N = 9
M = 10
values = [131, 98, 242, 231, 382, 224, 140, 209, 164]
edges = [(6, 8), (1, 6), (1, 4), (1, 3), (4, 7), (4, 9), (3, 7), (3, 9), (5, 9), (2, 5)]
print(smallest_initial_amount_of_money(N, M, values, edges))