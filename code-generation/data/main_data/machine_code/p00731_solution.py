def cliff_climbing(data):
    w, h = map(int, data.split()[:2])
    if w == 0 and h == 0:
        return -1
    matrix = [list(data.split()[i]) for i in range(2, 2+h)]
    
    def valid_position(x, y):
        return 0 <= x < w and 0 <= y < h
    
    def find_possible_moves(lx, ly, rx, ry):
        possible_moves = []
        for dx in range(-1, 2):
            nx = rx + dx
            for dy in range(-1, 2):
                ny = ry + dy
                if valid_position(nx, ny) and (dx != 0 or dy != 0) and abs(lx - nx) + abs(ly - ny) <= 3:
                    possible_moves.append((nx, ny))
        return possible_moves
    
    queue = [(0, [0]*w) for _ in range(2)]
    visited = set()
    
    while queue:
        steps, positions = queue.pop(0)
        lx, rx = positions
        ly, ry = 0, 0
        
        if matrix[ly][lx] == 'T' or matrix[ly][rx] == 'T':
            return steps
        
        visited.add((lx, ly, rx, ry))
        
        possible_moves_left = find_possible_moves(lx, ly, rx, ry)
        possible_moves_right = find_possible_moves(rx, ry, lx, ly)
        
        for nx, ny in possible_moves_left:
            if matrix[ny][nx] != 'X' and (nx, ny, rx, ry) not in visited:
                queue.append((steps + int(matrix[ny][nx]), [nx, rx]))
                visited.add((nx, ny, rx, ry))
        
        for nx, ny in possible_moves_right:
            if matrix[ny][nx] != 'X' and (lx, ly, nx, ny) not in visited:
                queue.append((steps + int(matrix[ny][nx]), [lx, nx]))
                visited.add((lx, ly, nx, ny))
    
    return -1