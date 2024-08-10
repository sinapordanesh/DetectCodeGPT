def longest_increasing_subsequence(N, A, edges):
    tree = {}
    for u, v in edges:
        if u not in tree:
            tree[u] = []
        if v not in tree:
            tree[v] = []
        tree[u].append(v)
        tree[v].append(u)
    
    def dfs(node, parent):
        longest = [1]
        for child in tree[node]:
            if child != parent:
                longest_child = dfs(child, node)
                if A[child-1] > A[node-1]:
                    longest.append(1 + longest_child)
        return max(longest)
    
    result = []
    for k in range(1, N+1):
        result.append(dfs(k, 0))
    
    return result

# Sample Input
N = 10
A = [1, 2, 5, 3, 4, 6, 7, 3, 2, 4]
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (3, 6), (6, 7), (1, 8), (8, 9), (9, 10)]

output = longest_increasing_subsequence(N, A, edges)
for line in output:
    print(line)