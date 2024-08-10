def shortest_path_length(w, h, maze):
    from collections import deque
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == w - 1 and y == h - 1:
            return dist
        
        if x - 1 >= 0 and not maze[y][x - 1] and not visited[y][x - 1]:
            queue.append((x - 1, y, dist + 1))
            visited[y][x - 1] = True
        
        if x + 1 < w and not maze[y][x] and not visited[y][x + 1]:
            queue.append((x + 1, y, dist + 1))
            visited[y][x + 1] = True
        
        if y - 1 >= 0 and not maze[y - 1][x] and not visited[y - 1][x]:
            queue.append((x, y - 1, dist + 1))
            visited[y - 1][x] = True
        
        if y + 1 < h and not maze[y][x] and not visited[y + 1][x]:
            queue.append((x, y + 1, dist + 1))
            visited[y + 1][x] = True
    
    return 0

# Sample Input
print(shortest_path_length(2, 3, [[1, 0], [0, 1], [1, 0]]))
print(shortest_path_length(9, 4, [[1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]]))