import sys


def main():
    a, b = [int(i) for i in sys.stdin.readline().split(' ')]
    print(int(a / b), a % b, '{:.10f}'.format(a / b))
    return


if __name__ == '__main__':
    main()

