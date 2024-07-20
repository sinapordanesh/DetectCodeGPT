def infinity_maze(robot_info):
    H, W, L = robot_info[0], robot_info[1], robot_info[2]
    maze = robot_info[3:]

    directions = ['N', 'E', 'S', 'W']
    delta_i = [-1, 0, 1, 0]
    delta_j = [0, 1, 0, -1]

    for i in range(H):
        for j in range(W):
            if maze[i][j] in directions:
                direction = directions.index(maze[i][j])
                row, col = i, j
                maze[i] = maze[i][:j] + '.' + maze[i][j+1:]
                break

    for _ in range(L):
        next_row = row + delta_i[direction]
        next_col = col + delta_j[direction]

        if 0 <= next_row < H and 0 <= next_col < W and maze[next_row][next_col] == '.':
            row, col = next_row, next_col
        else:
            direction = (direction + 1) % 4

    return f"{row+1} {col+1} {directions[direction]}"