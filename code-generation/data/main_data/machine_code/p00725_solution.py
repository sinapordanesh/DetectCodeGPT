def curling(data):
    width = data[0][0]
    height = data[0][1]
    board = data[1:]
    start = (0, 0)
    goal = (0, 0)

    for i in range(height):
        for j in range(width):
            if board[i][j] == 2:
                start = (i, j)
            elif board[i][j] == 3:
                goal = (i, j)

    def dfs(x, y, moves):
        if x < 0 or x >= height or y < 0 or y >= width or moves > 10:
            return -1
        if (x, y) == goal:
            return moves
        if board[x][y] == 1:
            return -1
        result = -1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x + dx
            new_y = y + dy
            while 0 <= new_x < height and 0 <= new_y < width and board[new_x][new_y] != 1:
                new_x += dx
                new_y += dy
            new_x -= dx
            new_y -= dy
            if (new_x, new_y) != (x, y):
                move = dfs(new_x, new_y, moves + 1)
                if move != -1 and (result == -1 or move < result):
                    result = move
        return result

    return dfs(start[0], start[1], 0)