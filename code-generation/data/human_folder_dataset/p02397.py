import sys


def main():
    while True:
        x, y = [int(i) for i in sys.stdin.readline().split(' ')]
        if x == 0 and y == 0:
            break
        elif x <= y:
            print(x, y)
        else:
            print(y, x)


if __name__ == '__main__':
    main()

