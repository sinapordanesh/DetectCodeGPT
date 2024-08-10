import sys


def main():
    while True:
        H, W = [int(i) for i in sys.stdin.readline().split()]
        if H == 0 and W == 0:
            break
        width = '#'
        for i in range(W - 1):
            width += '#'
        for i in range(H):
            print(width)
        print()


if __name__ == '__main__':
    main()

