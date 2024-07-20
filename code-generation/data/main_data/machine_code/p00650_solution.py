def lowest_cost(n, m, passageways):
    passageways.sort(key=lambda x: x[2])
    min_cost = float('inf')
    for i in range(m):
        temp_passageways = passageways[:i] + passageways[i+1:]
        group1 = set()
        group2 = set()
        visited = set()
        
        def dfs(room, group):
            if room in visited:
                return
            visited.add(room)
            group.add(room)
            for p in temp_passageways:
                if p[0] == room:
                    dfs(p[1], group)
        
        dfs(0, group1)
        
        if len(group1) == n:
            break
        
        for room in range(n):
            if room not in visited:
                dfs(room, group2)
        
        if len(group2) == n:
            min_cost = min(min_cost, passageways[i][2])
    
    return min_cost

print(lowest_cost(3, 2, [(0, 1, 2), (1, 2, 1)]))
print(lowest_cost(2, 1, [(0, 1, 100)]))
print(lowest_cost(2, 1, [(0, 1, 0)]))