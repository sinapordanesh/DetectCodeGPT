def marbles_in_box(N, parents):
    MOD = 1000000007
    children = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        children[parents[i-1]].append(i)
    
    def dfs(v):
        num_marbles = 1
        for child in children[v]:
            num_marbles += dfs(child)
        return num_marbles
    
    total_marbles = dfs(0)
    return total_marbles % MOD

# Sample Input 1
print(marbles_in_box(2, [0, 0]))

# Sample Input 2
print(marbles_in_box(5, [0, 1, 1, 0, 4]))

# Sample Input 3
print(marbles_in_box(31, [0, 1, 0, 2, 4, 0, 4, 1, 6, 4, 3, 9, 7, 3, 7, 2, 15, 6, 12, 10, 12, 16, 5, 3, 20, 1, 25, 20, 23, 24, 23]))