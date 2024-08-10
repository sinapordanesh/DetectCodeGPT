import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    import math
    a, b = input().split()
    x = int(a + b)
    sq = int(math.sqrt(x))
    if sq**2 == float(x):
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
