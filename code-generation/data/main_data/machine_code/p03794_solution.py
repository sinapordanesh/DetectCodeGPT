def count_minimal_d_value_ways(N, edges):
    MOD = 10**9 + 7
    
    adj_list = [[] for _ in range(N+1)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def dfs(v, p):
        dp = [0] * (N+1)
        dp[v] = 1
        for child in adj_list[v]:
            if child == p:
                continue
            dfs(child, v)
            dp[v] *= (dp[child] + 1)
            dp[v] %= MOD
        for child in adj_list[v]:
            if child == p:
                continue
            dp[v] = (dp[v] + dp[child] * pow(dp[child] + 1, MOD-2, MOD) * dp[child]) % MOD
        return dp[v]
    
    ans = dfs(1, 0)
    return ans

# Sample Input 1
print(count_minimal_d_value_ways(4, [(1, 2), (1, 3), (1, 4)]))

# Sample Input 2
print(count_minimal_d_value_ways(4, [(1, 2), (2, 3), (3, 4)]))

# Sample Input 3
print(count_minimal_d_value_ways(6, [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6)]))

# Sample Input 4
print(count_minimal_d_value_ways(10, [(2, 4), (2, 5), (8, 3), (10, 7), (1, 6), (2, 8), (9, 5), (8, 6), (10, 6)]))