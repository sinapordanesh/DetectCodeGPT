import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = list(input())
    S[:4] = "2018"

    print("".join(S))

if __name__ == '__main__':
    main()
