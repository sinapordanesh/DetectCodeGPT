def max_possible_edges(N, M, edges):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = set()
    for edge in edges:
        u, v = edge
        adj_list[u].add(v)
        adj_list[v].add(u)
    
    ans = 0
    for i in range(1, N+1):
        for j in adj_list[i]:
            for k in adj_list[j]:
                if k != i and k not in adj_list[i]:
                    ans += 1
    return ans

# Sample Input 1
N = 6
M = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
print(max_possible_edges(N, M, edges))

# Sample Input 2
N = 5
M = 5
edges = [(1, 2), (2, 3), (3, 1), (5, 4), (5, 1)]
print(max_possible_edges(N, M, edges))