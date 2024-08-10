def min_magic_needed(H, W, C_h, C_w, D_h, D_w, maze):
    from collections import deque
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def is_valid(x, y):
        return 0 <= x < H and 0 <= y < W
    
    def bfs():
        queue = deque([(C_h-1, C_w-1, 0)])
        visited = set([(C_h-1, C_w-1)])
        
        while queue:
            x, y, magic_used = queue.popleft()
            
            if x == D_h-1 and y == D_w-1:
                return magic_used
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if is_valid(new_x, new_y) and maze[new_x][new_y] == '.' and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, magic_used))
        
        return -1
    
    return bfs()