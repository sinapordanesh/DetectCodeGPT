def minimum_casts():
    H, W, K = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    start = None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
    
    min_casts = float('inf')
    
    def bfs(i, j):
        queue = deque([(i, j, 0)])
        visited = set()
        while queue:
            x, y, casts = queue.popleft()
            if grid[x][y] == 'S':
                return casts
            visited.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < H and 0 <= new_y < W and (new_x, new_y) not in visited and grid[new_x][new_y] != '#':
                    queue.append((new_x, new_y, casts+1))
                    
    min_casts = min(min_casts, bfs(start[0], start[1]))
    
    print(min_casts)

minimum_casts()