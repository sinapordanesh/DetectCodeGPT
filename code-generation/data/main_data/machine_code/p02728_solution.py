def number_of_ways(N, edges):
    mod = 10**9 + 7
    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a-1].append(b-1)
        adj_list[b-1].append(a-1)
        
    def dfs(node, parent, dp):
        dp[node][0] = dp[node][1] = 1
        for child in adj_list[node]:
            if child == parent:
                continue
            dfs(child, node, dp)
            dp[node][0] = dp[node][0] * dp[child][1] % mod
            dp[node][1] = dp[node][1] * (dp[child][0] + dp[child][1]) % mod
    
    dp = [[0, 0] for _ in range(N)]
    dfs(0, -1, dp)
    
    result = []
    for k in range(1, N+1):
        result.append(dp[k-1][1])
    
    return result

# Sample Input 1
N = 3
edges = [(1, 2), (1, 3)]
print(*number_of_ways(N, edges))

# Sample Input 2
N = 2
edges = [(1, 2)]
print(*number_of_ways(N, edges))

# Sample Input 3
N = 5
edges = [(1, 2), (2, 3), (3, 4), (3, 5)]
print(*number_of_ways(N, edges))

# Sample Input 4
N = 8
edges = [(1, 2), (2, 3), (3, 4), (3, 5), (3, 6), (6, 7), (6, 8)]
print(*number_of_ways(N, edges))