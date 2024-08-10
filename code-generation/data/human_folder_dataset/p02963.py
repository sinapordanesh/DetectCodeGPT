import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = input_int()
    x0 = y0 = 0
    x1 = 1
    x2 = 10**9
    y2 = -S % 10**9
    y1 = (S + y2) // 10**9

    print(x0, y0, x1, y1, x2, y2)
    return


if __name__ == "__main__":
    main()
