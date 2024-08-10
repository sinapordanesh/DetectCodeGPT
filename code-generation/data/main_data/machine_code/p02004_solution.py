def count_special_commands(sequence):
    count = 0
    special_command = False
    for command in sequence:
        if command == 'R':
            special_command = True
        elif command == 'L' and special_command:
            count += 1
            special_command = False
    return count

# Test the function
print(count_special_commands("RRRRLLLLRRRR"))
print(count_special_commands("RLLRLLLLRRRLLLRRR"))
print(count_special_commands("LR"))
print(count_special_commands("RRLRRLRRRRLRRLRRRRLRRLRRRRLRRLRR"))