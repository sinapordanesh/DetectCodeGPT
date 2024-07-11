import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    H = int(readline())
    W = int(readline())

    print((N - H + 1) * (N - W + 1))


if __name__ == '__main__':
    main()
