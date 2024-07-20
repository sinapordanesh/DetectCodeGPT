def emacs_editor(text, commands):
    cursor = [0, 0]
    buffer = ''
    edited_text = []

    for line in text:
        edited_text.append(list(line))

    for command in commands:
        if command == 'a':
            cursor[1] = 0
        elif command == 'e':
            cursor[1] = len(edited_text[cursor[0]])
        elif command == 'p':
            cursor[0] = max(0, cursor[0] - 1)
        elif command == 'n':
            cursor[0] = min(len(edited_text) - 1, cursor[0] + 1)
        elif command == 'f':
            if cursor[1] < len(edited_text[cursor[0]]):
                cursor[1] += 1
            elif cursor[0] < len(edited_text) - 1:
                cursor = [cursor[0] + 1, 0]
        elif command == 'b':
            if cursor[1] > 0:
                cursor[1] -= 1
            elif cursor[0] > 0:
                cursor = [cursor[0] - 1, len(edited_text[cursor[0] - 1])]
        elif command == 'd':
            if cursor[1] < len(edited_text[cursor[0]]):
                del edited_text[cursor[0]][cursor[1]]
            elif cursor[0] < len(edited_text) - 1:
                edited_text[cursor[0]] += edited_text[cursor[0] + 1]
                del edited_text[cursor[0] + 1]
        elif command == 'k':
            if cursor[1] == len(edited_text[cursor[0]]):
                if cursor[0] < len(edited_text) - 1:
                    edited_text[cursor[0]] += edited_text[cursor[0] + 1]
                    del edited_text[cursor[0] + 1]
                else:
                    buffer = '\n'
            else:
                buffer = ''.join(edited_text[cursor[0]][cursor[1]:])
                edited_text[cursor[0]] = edited_text[cursor[0]][:cursor[1]]
        elif command == 'y':
            if buffer == '\n':
                edited_text.insert(cursor[0] + 1, list('\n'))
                cursor = [cursor[0] + 1, 0]
            elif buffer:
                edited_text[cursor[0]] = edited_text[cursor[0]][:cursor[1]] + list(buffer) + edited_text[cursor[0]][cursor[1]:]
                cursor[1] += len(buffer)

    return ''.join([''.join(line) for line in edited_text])