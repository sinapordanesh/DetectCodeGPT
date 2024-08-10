import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *C = map(int, read().split())

    C.sort()

    ans = 0
    for i in range(N):
        ans = (ans + C[i] * (N - i + 1)) % MOD

    ans = ans * pow(2, 2 * N - 2, MOD) % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
