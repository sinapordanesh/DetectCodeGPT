def paint_squares(H, W, d):
    colors = ['R', 'Y', 'G', 'B']
    grid = [['' for _ in range(W)] for _ in range(H)]
    color_idx = 0
    
    for i in range(H):
        for j in range(W):
            grid[i][j] = colors[color_idx]
            color_idx = (color_idx + 1) % 4
            
    for i in range(H):
        print(''.join(grid[i]))