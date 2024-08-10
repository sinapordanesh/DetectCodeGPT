
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, v):
        self.stack.append(v)

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()


def run():
    n, q = [int(i) for i in input().split()]
    li = [Stack() for _ in range(n)]

    for _ in range(q):
        command = input()
        if command.startswith('0'):
            t, v = [int(i) for i in command[2:].split()]
            li[t].push(v)
        elif command.startswith('1'):
            t = int(command[2:])
            v = li[t].top()
            if v is not None:
                print(v)
        elif command.startswith('2'):
            t = int(command[2:])
            li[t].pop()
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

