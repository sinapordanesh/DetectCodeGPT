# import sys
# input = sys.stdin.readline
import collections
import itertools

def main():
    n, k = input_list()
    res = 0.0
    for v in range(n):
        i = v + 1
        t = 1.0
        ii = i
        while ii < k:
            ii *= 2
            t /= 2.0
        res += t

    res /= n
    print(res)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
