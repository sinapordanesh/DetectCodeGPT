def lexicographically_smallest_pair(N, edges):
    adj_list = [[] for _ in range(N+1)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def dfs(v, parent, depth):
        max_depth = depth
        for u in adj_list[v]:
            if u == parent:
                continue
            max_depth = max(max_depth, dfs(u, v, depth+1))
        return max_depth
    
    def binary_search():
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            max_depth = dfs(1, -1, 0)
            if max_depth <= mid:
                right = mid
            else:
                left = mid + 1
        return left
    
    A = binary_search()
    B = A - 1
    
    return A, B

# Sample Input
N = 7
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6), (6, 7)]
print(lexicographically_smallest_pair(N, edges))

N = 8
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (5, 8)]
print(lexicographically_smallest_pair(N, edges))

N = 10
edges = [(1, 2), (2, 3), (3, 4), (2, 5), (6, 5), (6, 7), (7, 8), (5, 9), (10, 5)]
print(lexicographically_smallest_pair(N, edges))