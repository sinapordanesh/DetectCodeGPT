def check_surprise_grid_possible(R, C, N, cells):
    grid = [[0 for _ in range(C)] for _ in range(R)]
    
    for r, c, num in cells:
        grid[r-1][c-1] = num
    
    for r in range(R):
        for c in range(C):
            if (r + c) % 2 == 0:
                grid[r][c] = 1e9
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                grid[r][c] = sum(grid[r]) - sum(grid[r][c])
    
    for r in range(R):
        for c in range(C):
            if c < C-1 and r < R-1:
                if grid[r][c] + grid[r+1][c+1] != grid[r][c+1] + grid[r+1][c]:
                    return "No"
    
    return "Yes" 

# Sample Input
print(check_surprise_grid_possible(2, 2, 3, [(1, 1, 0), (1, 2, 10), (2, 1, 20)])) # Yes
print(check_surprise_grid_possible(2, 3, 5, [(1, 1, 0), (1, 2, 10), (1, 3, 20), (2, 1, 30), (2, 3, 40)])) # No
print(check_surprise_grid_possible(2, 2, 3, [(1, 1, 20), (1, 2, 10), (2, 1, 0)])) # No
print(check_surprise_grid_possible(3, 3, 4, [(1, 1, 0), (1, 3, 10), (3, 1, 10), (3, 3, 20)])) # Yes
print(check_surprise_grid_possible(2, 2, 4, [(1, 1, 0), (1, 2, 10), (2, 1, 30), (2, 2, 20)])) # No