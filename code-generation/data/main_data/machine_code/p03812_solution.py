def find_winning_vertices(N, A, edges):
    adj_list = {}
    for i in range(N):
        adj_list[i+1] = []
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    winning_vertices = []
    for v in range(1, N+1):
        stones = A.copy()
        visited = [False] * (N+1)
        visited[v] = True
        stack = [v]
        takahashi_turn = True
        
        while stack:
            current_vertex = stack.pop()
            if takahashi_turn:
                stones[current_vertex - 1] = 0
            
            takahashi_turn = not takahashi_turn
            for neighbor in adj_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        
        if sum(stones) == 0:
            winning_vertices.append(v)
    
    return winning_vertices

# Sample Input 1
N = 3
A = [1, 2, 3]
edges = [(1, 2), (2, 3)]
print(find_winning_vertices(N, A, edges))

# Sample Input 2
N = 5
A = [5, 4, 1, 2, 3]
edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
print(find_winning_vertices(N, A, edges))

# Sample Input 3
N = 3
A = [1, 1, 1]
edges = [(1, 2), (2, 3)]
print(find_winning_vertices(N, A, edges))