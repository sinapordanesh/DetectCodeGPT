def offline_text_editor(texts):
    for text in texts:
        initial_text = text[0]
        commands = text[1:]
        cursor = 0
        
        for command in commands:
            if command == "forward char":
                cursor = min(cursor + 1, len(initial_text))
            elif command == "forward word":
                cursor = initial_text.find(" ", cursor)
                if cursor == -1:
                    cursor = len(initial_text)
            elif command == "backward char":
                cursor = max(cursor - 1, 0)
            elif command == "backward word":
                cursor = initial_text.rfind(" ", 0, cursor)
                if cursor == -1:
                    cursor = 0
            elif command.startswith("insert "):
                text_to_insert = command[7:-1]
                initial_text = initial_text[:cursor] + text_to_insert + initial_text[cursor:]
                cursor += len(text_to_insert)
            elif command == "delete char":
                if cursor < len(initial_text):
                    initial_text = initial_text[:cursor] + initial_text[cursor+1:]
            elif command == "delete word":
                end_of_left_word = initial_text.rfind(" ", 0, cursor)
                start_of_right_word = initial_text.find(" ", cursor)
                if end_of_left_word == -1:
                    end_of_left_word = 0
                if start_of_right_word == -1:
                    start_of_right_word = len(initial_text)
                initial_text = initial_text[:end_of_left_word] + initial_text[start_of_right_word:]
                cursor = end_of_left_word
        
        print(initial_text[:cursor] + "^" + initial_text[cursor:]) 

# Sample Input
offline_text_editor([["A sample input", "forward word", "delete char", "forward word", "delete char", "forward word", "delete char", "backward word", "backward word", "forward word"],["Hallow, Word.", "forward char", "delete word", 'insert "ello, "', "forward word", "backward char", "backward char", 'insert "l"'],["ple Offline Text Editor", "forward word", "backward word", "delete word"]])