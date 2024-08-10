def max_moves_to_make(H, W, maze):
    def bfs(x, y):
        queue = [(x, y, 0)]
        visited = [[False for _ in range(W)] for _ in range(H)]
        visited[x][y] = True
        max_moves = 0
        
        while queue:
            i, j, moves = queue.pop(0)
            max_moves = max(max_moves, moves)
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < H and 0 <= nj < W and maze[ni][nj] == '.' and not visited[ni][nj]:
                    queue.append((ni, nj, moves + 1))
                    visited[ni][nj] = True
        
        return max_moves
    
    max_moves = 0
    for i in range(H):
        for j in range(W):
            if maze[i][j] == '.':
                max_moves = max(max_moves, bfs(i, j))
    
    return max_moves

# Sample Input 1
print(max_moves_to_make(3, 3, ['...', '...', '...']))

# Sample Input 2
print(max_moves_to_make(3, 5, ['...#.', '.#.#.', '.#...']))