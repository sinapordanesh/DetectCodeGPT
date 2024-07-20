# import sys
# input = sys.stdin.readline
import collections
import itertools


def main():
    n = int(input())
    x = input_list()
    sx = list(sorted(x))
    h = n//2
    a1 = sx[h-1]
    a2 = sx[h]
    for v in x:
        if v <= a1:
            print(a2)
        else:
            print(a1)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
