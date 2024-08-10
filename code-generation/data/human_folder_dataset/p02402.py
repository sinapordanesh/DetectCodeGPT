import sys


def main():
    sys.stdin.readline()
    list1 = [int(i) for i in sys.stdin.readline().split()]
    print(min(list1), max(list1), sum(list1))


if __name__ == '__main__':
    main()

