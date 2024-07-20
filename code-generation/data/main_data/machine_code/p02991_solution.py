from collections import deque

def ken_ken_pa(N, M, edges, S, T):
    graph = {i: [] for i in range(1, N+1)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    queue = deque([(S, 0)])
    visited = set()
    
    while queue:
        node, steps = queue.popleft()
        
        if node == T:
            return steps // 3
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor in graph[node]:
            queue.append((neighbor, steps + 1))
    
    return -1

# Sample Input 1
print(ken_ken_pa(4, 4, [(1, 2), (2, 3), (3, 4), (4, 1)], 1, 3))

# Sample Input 2
print(ken_ken_pa(3, 3, [(1, 2), (2, 3), (3, 1)], 1, 2))

# Sample Input 3
print(ken_ken_pa(2, 0, [], 1, 2))

# Sample Input 4
print(ken_ken_pa(6, 8, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 4), (1, 5), (4, 6)], 1, 6))