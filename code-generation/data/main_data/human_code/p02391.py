import sys


def main():
    input_str = sys.stdin.readline()
    a, b = [int(i) for i in input_str.split(' ')]
    if a > b:
        print('a > b')
    elif a < b:
        print('a < b')
    else:
        print('a == b')

    return


if __name__ == '__main__':
    main()

