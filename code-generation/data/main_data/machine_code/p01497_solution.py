def bubble_puzzle(grid):
    grid = [list(map(int, row.split())) for row in grid]
    
    def click(grid):
        next_grid = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                next_grid[i][j] += grid[i][j]
                if grid[i][j] >= 5:
                    next_grid[i][j] -= 5
                    if i > 0:
                        next_grid[i-1][j] += 1
                    if i < 3:
                        next_grid[i+1][j] += 1
                    if j > 0:
                        next_grid[i][j-1] += 1
                    if j < 3:
                        next_grid[i][j+1] += 1
        return next_grid
    
    def check(grid):
        for i in range(4):
            for j in range(4):
                if grid[i][j] >= 5:
                    return False
        return True
    
    clicks = 0
    while not check(grid):
        grid = click(grid)
        clicks += 1
        if clicks > 5:
            return -1
    return clicks

print(bubble_puzzle(["4 4 4 4", "4 4 4 4", "4 4 4 4", "4 4 4 4"]))
print(bubble_puzzle(["2 4 4 1", "2 4 4 1", "2 4 4 1", "2 4 4 1"]))
print(bubble_puzzle(["2 4 3 4", "2 2 4 4", "3 3 2 2", "2 3 3 3"]))