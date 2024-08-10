def repaint_grid(N, grid):
    def check_all_black(grid):
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    return False
        return True

    def repaint_column(j):
        colors = [grid[i][j] for i in range(N)]
        for i in range(N):
            grid[i][j] = '.'

    operations = 0
    while not check_all_black(grid):
        max_black = 0
        max_black_index = 0
        for j in range(N):
            count_black = grid[j].count('#')
            if count_black > max_black:
                max_black = count_black
                max_black_index = j
        if max_black == 0:
            return -1
        repaint_column(max_black_index)
        operations += 1

    return operations

N = int(input())
grid = [list(input()) for _ in range(N)]
print(repaint_grid(N, grid))