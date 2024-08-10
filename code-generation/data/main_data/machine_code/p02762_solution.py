def friend_candidates(N, M, K, friendships, blockships):
    graph = {}
    for i in range(1, N+1):
        graph[i] = set()
    
    for a, b in friendships:
        graph[a].add(b)
        graph[b].add(a)
        
    for c, d in blockships:
        if d in graph[c]:
            graph[c].remove(d)
        if c in graph[d]:
            graph[d].remove(c)
    
    def dfs(u, target, visited):
        if u == target:
            return True
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                if dfs(v, target, visited):
                    return True
        return False
    
    result = []
    for i in range(1, N+1):
        count = 0
        for j in range(1, N+1):
            if i != j and j not in graph[i] and (dfs(i, j, set()) or dfs(j, i, set())):
                count += 1
        result.append(count)
    
    return ' '.join(map(str, result))

# Input
N, M, K = map(int, input().split())
friendships = [tuple(map(int, input().split())) for _ in range(M)]
blockships = [tuple(map(int, input().split())) for _ in range(K)]

# Output
print(friend_candidates(N, M, K, friendships, blockships))