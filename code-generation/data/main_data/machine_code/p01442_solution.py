def mysterious_maze(H, W, N, program, maze):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # East, South, West, North

    def turn(direction, command):
        if command == 'L':
            return (direction - 1) % 4
        else:
            return (direction + 1) % 4

    def move(position, direction):
        new_position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
        if 0 <= new_position[0] < H and 0 <= new_position[1] < W and maze[new_position[0]][new_position[1]] != '#':
            return new_position
        return position

    entrance = None
    for i in range(H):
        for j in range(W):
            if maze[i][j] == 'S':
                entrance = (i, j)
                break
        if entrance:
            break

    current_position = entrance
    current_direction = 3 # Facing North
    program_index = 0

    while program_index < N:
        command = program[program_index]
        if command in ['L', 'R']:
            current_direction = turn(current_direction, command)
        else:
            current_position = move(current_position, current_direction)
            if maze[current_position[0]][current_position[1]] == 'G':
                return "Yes"
        program_index += 1

    return "No"

# Sample Input
print(mysterious_maze(2, 2, 1, "L", ["G.", "#S"]))
print(mysterious_maze(2, 2, 2, "RR", ["G.", ".S"]))
print(mysterious_maze(3, 3, 6, "LLLLLL", ["G#.", "...", ".#S"]))