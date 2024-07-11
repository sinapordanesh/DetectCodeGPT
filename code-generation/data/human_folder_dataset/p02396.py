import sys


def main():
    i = 1
    while True:
        x = int(sys.stdin.readline())
        if x != 0:
            print("Case {0}: {1}".format(i, x))
            i += 1
        else:
            break
    return


if __name__ == '__main__':
    main()

