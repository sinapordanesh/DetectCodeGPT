def go_around_labyrinth(N, M, grid):
    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M or grid[x][y] == '#':
            return
        if grid[x][y] == 'N':
            found_treasure[0] = True
            return
        grid[x][y] = '#'
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

    found_treasure = [False]
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'N':
                dfs(i, j)
    return "YES" if found_treasure[0] else "NO"