def count_ways_to_divide_vertices(N, edges):
    MOD = 10**9 + 7
    def dfs(u, p, g):
        res = 1
        for v in g[u]:
            if v == p:
                continue
            res *= dfs(v, u, g)
            res %= MOD
        return res + 1
    g = [[] for _ in range(N)]
    for x, y in edges:
        g[x-1].append(y-1)
        g[y-1].append(x-1)
    ans = 1
    for i in range(N):
        if len(g[i]) == 1:
            ans *= dfs(i, -1, g)
            ans %= MOD
    return ans

# Sample Input 1
print(count_ways_to_divide_vertices(4, [[1, 2], [2, 3], [3, 4]]))

# Sample Input 2
print(count_ways_to_divide_vertices(4, [[1, 2], [1, 3], [1, 4]]))

# Sample Input 3
print(count_ways_to_divide_vertices(6, [[1, 2], [1, 3], [3, 4], [1, 5], [5, 6]]))

# Sample Input 4
print(count_ways_to_divide_vertices(10, [[8, 5], [10, 8], [6, 5], [1, 5], [4, 8], [2, 10], [3, 6], [9, 2], [1, 7]]))