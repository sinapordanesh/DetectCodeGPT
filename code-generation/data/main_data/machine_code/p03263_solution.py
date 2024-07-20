def maximize_even_cells(H, W, grid):
    def valid_move(y, x):
        return 1 <= y <= H and 1 <= x <= W
    
    def make_move(y1, x1, y2, x2):
        nonlocal operations
        operations.append((y1, x1, y2, x2))
        grid[y2-1][x2-1] += 1
        grid[y1-1][x1-1] -= 1
    
    operations = []
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] % 2 != 0:
                if i % 2 == 0:
                    if valid_move(i+1, j+1):
                        make_move(i+1, j+1, i+2, j+1)
                    elif valid_move(i+1, j):
                        make_move(i+1, j+1, i+1, j)
                else:
                    if valid_move(i+1, j):
                        make_move(i+1, j+1, i+1, j)
                    elif valid_move(i+1, j+2):
                        make_move(i+1, j+1, i+1, j+2)
    
    print(len(operations))
    for op in operations:
        print(*op)

# Sample Input
H, W = 2, 3
grid = [
    [1, 2, 3],
    [0, 1, 1]
]
maximize_even_cells(H, W, grid)