import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, c = map(int, readline().split())

    if a == b == c:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
