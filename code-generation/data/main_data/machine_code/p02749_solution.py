def find_permutation(N, edges):
    adj_list = {}
    for i in range(1, N + 1):
        adj_list[i] = []
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    visited = [False] * (N + 1)
    permutation = [0] * (N + 1)
    
    def dfs(node, parent, val):
        visited[node] = True
        permutation[node] = val
        for child in adj_list[node]:
            if child != parent:
                for i in range(1, N + 1):
                    if i != val and (i + val) % 3 != 0:
                        dfs(child, node, i)
                        break
    
    dfs(1, 0, 1)
    
    return " ".join(str(permutation[i]) for i in range(1, N + 1)) if all(visited[1:]) else "-1"

# Sample Input
N = 5
edges = [(1, 2), (1, 3), (3, 4), (3, 5)]

print(find_permutation(N, edges))