def maximize_score(N, edges, c):
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
    
    result = []
    visited = [False] * N
    
    def dfs(node):
        visited[node] = True
        result.append(c[node])
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(0)
    
    return sum(min(result[i], result[i+1]) for i in range(N-1)), result

# Sample Input 1
N = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
c = [1, 2, 3, 4, 5]
print(maximize_score(N, edges, c))

# Sample Input 2
N = 5
edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
c = [3141, 59, 26, 53, 59]
print(maximize_score(N, edges, c))