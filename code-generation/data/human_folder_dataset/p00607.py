import sys


class Cursor:
    BOL = (0,1)

    def __init__(self, text):
        assert isinstance(text, list)
        self.text = text

        for i in range(len(self.text)):
            self.text[i] = list(self.text[i])

        self.buffer = ""
        self.line = 1
        self.pos = self.BOL

    def _check(self):
        assert self.line > 0

    def _get_pos_end_of_line(self):
        last_char = len(self.text[self.line-1])
        return (last_char, last_char+1)

    def has_prev_line(self):
        return self.line > 1

    def has_next_line(self):
        return self.line < len(self.text)

    def beginning_of_line(self):
        self.pos = self.BOL

    def end_of_line(self):
        self.pos = self._get_pos_end_of_line()

    def prev_line(self):
        if self.has_prev_line():
            self.line -= 1

    def next_line(self):
        if self.has_next_line():
            self.line += 1

    def right_pos(self):
        if self._get_pos_end_of_line() != self.pos:
            self.pos = (self.pos[0] + 1, self.pos[1] + 1)
        else:
            if self.has_next_line():
                self.line += 1
                self.pos = self.BOL

    def left_pos(self):
        if self.BOL != self.pos:
            self.pos = (self.pos[0] - 1, self.pos[1] - 1)
        else:
            if self.has_prev_line():
                self.line -= 1
                self.pos = self._get_pos_end_of_line()

    def remove_current_pos(self):
        if self._get_pos_end_of_line() != self.pos:
            self.text[self.line-1] = self.text[self.line-1][:self.pos[0]] + self.text[self.line-1][self.pos[1]:]
        else:
            if self.has_next_line():
                self.text[self.line-1][self.pos[0]:self.pos[0]] = self.text[self.line]
                self.text.pop(self.line)

    def remove_to_end_of_line(self):
        if self._get_pos_end_of_line() == self.pos:
            if self.has_next_line():
                self.remove_current_pos()
                self.buffer = '\n'
        else:
            self.buffer = self.text[self.line - 1][self.pos[0]:]
            self.text[self.line - 1] = self.text[self.line - 1][:self.pos[0]]
            self.pos = self._get_pos_end_of_line()

    def paste(self):
        if self.buffer:
            if self.buffer == '\n':
                prev = self.text[self.line - 1][:self.pos[0]]
                next = self.text[self.line - 1][self.pos[0]:]

                self.text[self.line - 1] = prev
                self.text.insert(self.line, next)

                self.line += 1
                self.pos = self.BOL
            else:
                self.text[self.line - 1][self.pos[0]:self.pos[0]] = self.buffer
                self.pos = (self.pos[0] + len(self.buffer), self.pos[1] + len(self.buffer))

    def print(self):
        for t in self.text:
            print("".join(t))


class Editor:
    def __init__(self, text):
        assert isinstance(text, list)
        self.cursor = Cursor(text)

    def process(self, commands):
        if not isinstance(commands, list):
            commands = [commands]

        for command in commands:
            self._process(command)

        self.cursor.print()

    def _process(self, command):
        if command == 'a':
            self.cursor.beginning_of_line()
        elif command == 'e':
            self.cursor.end_of_line()
        elif command == 'p':
            self.cursor.prev_line()
            self.cursor.beginning_of_line()
        elif command == 'n':
            self.cursor.next_line()
            self.cursor.beginning_of_line()
        elif command == 'f':
            self.cursor.right_pos()
        elif command == 'b':
            self.cursor.left_pos()
        elif command == 'd':
            self.cursor.remove_current_pos()
        elif command == 'k':
            self.cursor.remove_to_end_of_line()
        elif command == 'y':
            self.cursor.paste()




def load_input():
    inputs = []
    while True:
        try:
            inputs.append(input())
        except EOFError:
            return inputs

def split_end_of_text(inputs):
    assert inputs
    assert 'END_OF_TEXT' in inputs

    for i in range(len(inputs)):
        if inputs[i] == 'END_OF_TEXT':
            return inputs[:i], inputs[i+1:]
    else:
        print("DO NOT DETECT END_OF_TEXT. got:", inputs)
        sys.exit(1)

    
def main():
    inputs = load_input()
    text, commands = split_end_of_text(inputs)

    # Attacking
    assert 'END_OF_TEXT' not in text
    assert 'END_OF_TEXT' not in commands

    editor = Editor(text)
    editor.process(commands)

main()

