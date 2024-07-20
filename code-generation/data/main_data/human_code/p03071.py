import math


def main():
    # n = int(input())
    a, b = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]
    count = 0
    if a < b:
        count += b
        b = b - 1
    else:
        count += a
        a = a - 1
    if a < b:
        count += b
        b = b - 1
    else:
        count += a
        a = a - 1

    print(count)


if __name__ == '__main__':
    main()
