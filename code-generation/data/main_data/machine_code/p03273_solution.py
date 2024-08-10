def compress_grid():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    rows_to_delete = []
    cols_to_delete = []
    
    for i in range(H):
        if '.' not in grid[i]:
            rows_to_delete.append(i)
    
    for j in range(W):
        if all(grid[i][j] == '.' for i in range(H)):
            cols_to_delete.append(j)
    
    compressed_grid = []
    
    for i in range(H):
        if i not in rows_to_delete:
            compressed_row = ''
            for j in range(W):
                if j not in cols_to_delete:
                    compressed_row += grid[i][j]
            compressed_grid.append(compressed_row)
    
    for row in compressed_grid:
        print(row)

compress_grid()