from collections import deque

def main():
    lst = deque()

    n = int(input())

    for _ in range(n):
        cmd = input().split()

        if 'insert' == cmd[0]:
            lst.appendleft(cmd[1])
        if 'delete' == cmd[0]:
            try:
                lst.remove(cmd[1])
            except:
                pass
        if 'deleteFirst' == cmd[0]:
            lst.popleft()
        if 'deleteLast' == cmd[0]:
            lst.pop()

    sep = ''
    for n in lst:
        print(sep+n, end='')
        sep = ' '
    print()

if __name__ == '__main__':
    main()

