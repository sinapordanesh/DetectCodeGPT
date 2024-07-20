def magical_girl_ability(H, W, D, A, Q, tests):
    grid = {}
    for i in range(H):
        for j in range(W):
            grid[A[i][j]] = (i, j)
    
    def magic_points(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    result = []
    for test in tests:
        L, R = test
        x1, y1 = grid[L]
        x2, y2 = grid[R]
        total_points = 0
        
        while A[x1][y1] != R:
            x = A[x1][y1]
            next_x, next_y = grid[x+D]
            total_points += magic_points(x1, y1, next_x, next_y)
            x1, y1 = next_x, next_y
        
        result.append(total_points)
    
    return result