import sys


def main():
    while True:
        H, W = [int(i) for i in sys.stdin.readline().split()]
        if H == 0 and W == 0:
            break
        top_bottom_line = '#'
        insider_line = '#'
        for i in range(W - 1):
            top_bottom_line += '#'
        for i in range(W - 2):
            insider_line += '.'
        insider_line += '#'
        print(top_bottom_line)
        for i in range(H - 2):
            print(insider_line)
        print(top_bottom_line)
        print()
    return


if __name__ == '__main__':
    main()

