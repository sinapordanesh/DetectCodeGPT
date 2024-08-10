#!/usr/bin/env python3


def main():
    import sys

    input = sys.stdin.readline

    N, Z, W = map(int, input().split())
    a = [int(x) for x in input().split()]

    if N == 1:
        print(abs(a[-1] - W))
    else:
        print(max(abs(a[-1] - W), abs(a[-2] - a[-1])))


if __name__ == '__main__':
    main()
