import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    A = input()
    B = input()
    C = input()
    ans = 0

    for a, b, c, in zip(A, B, C):
        s = {a, b, c}
        ans += len(s) - 1

    print(ans)

if __name__ == '__main__':
    main()
