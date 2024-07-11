import sys


def main():
    input_str = sys.stdin.readline()
    a, b, c = [int(i) for i in input_str.split(' ')]
    if a < b & b < c:
        print('Yes')
    else:
        print('No')
    return


if __name__ == '__main__':
    main()

