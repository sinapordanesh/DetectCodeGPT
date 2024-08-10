MOD = 10**9 + 7
def paint_vertices(N, edges):
    adj_list = [[] for _ in range(N)]
    for x, y in edges:
        adj_list[x - 1].append(y - 1)
        adj_list[y - 1].append(x - 1)
    
    dp = [[0, 0] for _ in range(N)]
    
    def dfs(node, parent):
        dp[node][0] = dp[node][1] = 1
        for nei in adj_list[node]:
            if nei == parent:
                continue
            dfs(nei, node)
            dp[node][0] = dp[node][0] * (dp[nei][0] + dp[nei][1]) % MOD
            dp[node][1] = dp[node][1] * dp[nei][0] % MOD
    
    dfs(0, -1)
    return (dp[0][0] + dp[0][1]) % MOD

# Sample Input
N = 3
edges = [(1, 2), (2, 3)]
print(paint_vertices(N, edges))

N = 4
edges = [(1, 2), (1, 3), (1, 4)]
print(paint_vertices(N, edges))

N = 1
edges = []
print(paint_vertices(N, edges))

N = 10
edges = [(8, 5), (10, 8), (6, 5), (1, 5), (4, 8), (2, 10), (3, 6), (9, 2), (1, 7)]
print(paint_vertices(N, edges))