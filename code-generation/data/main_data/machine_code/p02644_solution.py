def min_strokes_to_reach_destination(H, W, K, x1, y1, x2, y2, grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[x1-1][y1-1] = True
    
    queue = [(x1-1, y1-1, 0)]
    
    while queue:
        x, y, steps = queue.pop(0)
        
        if x == x2-1 and y == y2-1:
            return steps
        
        for dx, dy in directions:
            for i in range(1, K+1):
                new_x, new_y = x + dx*i, y + dy*i
                if 0 <= new_x < H and 0 <= new_y < W and not visited[new_x][new_y] and grid[new_x][new_y] == '.':
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, steps+1))
    
    return -1

# Sample Input 1
print(min_strokes_to_reach_destination(3, 5, 2, 3, 2, 3, 4, ['.....', '.@..@', '..@..']))

# Sample Input 2
print(min_strokes_to_reach_destination(1, 6, 4, 1, 1, 1, 6, ['......']))

# Sample Input 3
print(min_strokes_to_reach_destination(3, 3, 1, 2, 1, 2, 3, ['.@.', '.@.', '.@.']))