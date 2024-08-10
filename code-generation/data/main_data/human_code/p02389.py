import sys


def main():
    a, b = sys.stdin.readline().split(" ")
    a, b = int(a), int(b)
    print("{0} {1}".format(a*b, a*2 + b*2))
    return


if __name__ == '__main__':
    main()

