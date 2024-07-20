import sys

input = sys.stdin.buffer.readline
in_n = lambda: int(input())
in_nn = lambda: map(int, input().split())
in_s = lambda: input().rstrip().decode('utf-8')
in_map = lambda: [s == ord('.') for s in input() if s != ord('\n')]

MOD = 10**9 + 7
INF = 8 * 10**18


def main():

    N = in_n()
    S = in_s()

    ans = 0
    for i in range(1, N - 1):
        v1 = set(S[:i])
        v2 = set(S[i:])
        ans = max(ans, len(v1 & v2))

    print(ans)


if __name__ == '__main__':
    main()
