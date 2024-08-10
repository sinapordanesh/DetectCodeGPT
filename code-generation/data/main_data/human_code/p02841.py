import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    m1, d1 = map(int, readline().split())
    m2, d2 = map(int, readline().split())

    if m1 != m2:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
