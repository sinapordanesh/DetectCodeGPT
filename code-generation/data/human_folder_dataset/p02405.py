import sys


def main():
    while True:
        H, W = map(int, sys.stdin.readline().split())
        if H == 0 and W == 0: break
        for h in range(H):
            for w in range(W):
                if h % 2 == 0:
                    if w % 2 == 0:
                        print('#', end='')
                    else:
                        print('.', end='')
                else:
                    if w % 2 == 0:
                        print('.', end='')
                    else:
                        print('#',end='')
            print()
        print()
    return


if __name__ == '__main__':
    main()

