import math


def main():
    n = int(input())
    # a, b = map(int, input().split())
    h = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in rane(n)]

    count = 1
    maxi = h[0]
    for i in range(1, n):
        if h[i] >= h[i-1] and h[i] >= maxi:
            count += 1
            maxi = h[i]
    print(count)


if __name__ == '__main__':
    main()
