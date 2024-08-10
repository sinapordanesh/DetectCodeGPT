import sys


def main():
    input_str = sys.stdin.readline()
    list1 = [int(i) for i in input_str.split(' ')]
    list1.sort()
    print('{0[0]} {0[1]} {0[2]}'.format(list1))
    return


if __name__ == '__main__':
    main()

