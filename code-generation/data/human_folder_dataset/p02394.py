import sys


def main():
    input_str = sys.stdin.readline()
    W, H, x, y, r = [int(i) for i in input_str.split(' ')]
    upper = H >= y + r
    lower = y - r >= 0
    left = x - r >= 0
    right = x + r <= W
    if upper & lower & left & right:
        print('Yes')
    else:
        print('No')
    return


if __name__ == '__main__':
    main()

