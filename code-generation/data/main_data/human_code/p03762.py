import sys

input = sys.stdin.buffer.readline
in_n = lambda: int(input())
in_nn = lambda: map(int, input().split())
in_s = lambda: input().rstrip().decode('utf-8')
in_map = lambda: [s == ord('.') for s in input() if s != ord('\n')]

MOD = 10**9 + 7
INF = 8 * 10**18


def main():

    N, M = in_nn()
    X = list(in_nn())
    Y = list(in_nn())

    x_tsum = [0] * (N + 1)
    for i in range(N):
        x_tsum[i + 1] += x_tsum[i] + X[i]
        x_tsum[i + 1] %= MOD

    x_sum = 0
    for i in range(1, N):
        x_sum += X[i] * i - x_tsum[i]
        x_sum %= MOD

    y_tsum = [0] * (M + 1)
    for i in range(M):
        y_tsum[i + 1] += y_tsum[i] + Y[i]
        y_tsum[i + 1] %= MOD

    y_sum = 0
    for i in range(1, M):
        y_sum += Y[i] * i - y_tsum[i]
        y_sum %= MOD

    print(x_sum * y_sum % MOD)


if __name__ == '__main__':
    main()
