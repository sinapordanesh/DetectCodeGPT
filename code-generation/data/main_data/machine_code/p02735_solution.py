def min_operations_needed(H, W, grid):
    operations = 0
    for i in range(H):
        for j in range(W):
            if (i == 0 and j == 0) or (i == H-1 and j == W-1):
                if grid[i][j] == '#':
                    operations += 1
            elif (i == 0 and grid[i][j] == '.') or (j == 0 and grid[i][j] == '.'):
                operations += 1
    return operations

# Sample Input 1
print(min_operations_needed(3, 3, ['.##', '.#.', '##.']))

# Sample Input 2
print(min_operations_needed(2, 2, ['#.', '.#']))

# Sample Input 3
print(min_operations_needed(4, 4, ['..##', '#...', '###.', '###.']))

# Sample Input 4
print(min_operations_needed(5, 5, ['.#.#.', '#.#.#', '.#.#.', '#.#.#', '.#.#.']))