def paint_squares(H, W, N, colors):
    grid = [[0]*W for _ in range(H)]
    cur_color = 1
    cur_cnt = 0
    
    for i in range(H):
        for j in range(W):
            grid[i][j] = cur_color
            cur_cnt += 1
            if cur_cnt == colors[cur_color-1]:
                cur_color += 1
                cur_cnt = 0
    
    for row in grid:
        print(*row)