def number_of_operations(H, W, grid):
    def is_valid(i, j):
        return 0 <= i < H and 0 <= j < W
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    operations = 0
    while True:
        changed = False
        new_grid = [['.' for _ in range(W)] for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '#':
                    new_grid[i][j] = '#'
                else:
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if is_valid(ni, nj) and grid[ni][nj] == '#':
                            new_grid[i][j] = '#'
                            changed = True
                            break
        if not changed:
            break
        operations += 1
        grid = new_grid
        
    return operations

# Sample Input 1
print(number_of_operations(3, 3, ['...', '.#.', '...']))

# Sample Input 2
print(number_of_operations(6, 6, ['..#..#', '......', '#..#..', '......', '.#....', '....#.']))