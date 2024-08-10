def robot_position(commands):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    x, y = 1, 1
    
    for command in commands:
        if command[0] == "FORWARD":
            steps = int(command[1])
            x += directions[current_direction][0] * steps
            y += directions[current_direction][1] * steps
        elif command[0] == "BACKWARD":
            steps = int(command[1])
            x -= directions[current_direction][0] * steps
            y -= directions[current_direction][1] * steps
        elif command[0] == "RIGHT":
            current_direction = (current_direction + 1) % 4
        elif command[0] == "LEFT":
            current_direction = (current_direction - 1) % 4
        elif command[0] == "STOP":
            return (x, y)

# Sample Input
commands = [("FORWARD", "3"), ("RIGHT", ""), ("FORWARD", "5"), ("LEFT", ""), ("BACKWARD", "2"), ("STOP", "")]
print(robot_position(commands))

commands = [("FORWARD", "2"), ("STOP", "")]
print(robot_position(commands))