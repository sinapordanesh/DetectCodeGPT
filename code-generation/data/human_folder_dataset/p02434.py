def run():
    n, q = [int(x) for x in input().split()]
    ls = [[] for _ in range(n)]

    for _ in range(q):
        command = input()
        if command.startswith('0'):
            i, j = [int(x) for x in command[2:].split()]
            ls[i].append(j)
        elif command.startswith('1'):
            i = int(command[2:])
            print(" ".join([str(x) for x in ls[i]]))
        elif command.startswith('2'):
            i = int(command[2:])
            ls[i] = []
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

