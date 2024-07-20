def transformation(str, commands):
    for command in commands:
        if command[0] == 'print':
            print(str[command[1]:command[2]+1])
        elif command[0] == 'reverse':
            str = str[:command[1]] + str[command[1]:command[2]+1][::-1] + str[command[2]+1:]
        elif command[0] == 'replace':
            str = str[:command[1]] + command[3] + str[command[2]+1:]
            
# Sample Input 1
str1 = "abcde"
commands1 = [("replace", 1, 3, "xyz"), ("reverse", 0, 2), ("print", 1, 4)]
transformation(str1, commands1)

# Sample Input 2
str2 = "xyz"
commands2 = [("print", 0, 2), ("replace", 0, 2, "abc"), ("print", 0, 2)]
transformation(str2, commands2)