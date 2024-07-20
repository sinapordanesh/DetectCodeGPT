def diagonal_letters():
    grid = [input() for _ in range(3)]
    print(grid[0][0] + grid[1][1] + grid[2][2])

diagonal_letters()