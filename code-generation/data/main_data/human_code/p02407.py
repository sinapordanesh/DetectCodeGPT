import sys


def main():
    sys.stdin.readline()
    list1 = list(map(str, sys.stdin.readline().split()))
    list.reverse(list1)
    print(' '.join(list1))

    return


if __name__ == '__main__':
    main()

