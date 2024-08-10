def expected_holeyness(N, edges):
    MOD = 10**9 + 7
    adj_list = {i: [] for i in range(1, N+1)}
    for edge in edges:
        a, b = edge
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def dfs(node, parent):
        black_count = 1
        white_count = 0
        for child in adj_list[node]:
            if child == parent:
                continue
            child_black, child_white = dfs(child, node)
            black_count *= (child_black + child_white) % MOD
            white_count += (child_white + 1) % MOD
        return black_count % MOD, white_count % MOD
    
    black, white = dfs(1, 0)
    return (2 * white) % MOD

# Sample Input
N = 3
edges = [(1, 2), (2, 3)]
print(expected_holeyness(N, edges))

N = 4
edges = [(1, 2), (2, 3), (3, 4)]
print(expected_holeyness(N, edges))

N = 4
edges = [(1, 2), (1, 3), (1, 4)]
print(expected_holeyness(N, edges))

N = 7
edges = [(4, 7), (3, 1), (2, 6), (5, 2), (7, 1), (2, 7)]
print(expected_holeyness(N, edges))