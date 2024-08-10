import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())
    H = [0] + list(map(int, readline().split())) + [0]

    dp = [[INF] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 0

    for i in range(1, N + 1):
        dp[i][1] = H[i]
        for j in range(2, i + 1):
            for k in range(1, i):
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + max(0, H[i] - H[k]))

    ans = INF
    for i in range(1, N + 1):
        ans = min(ans, dp[i][N - K])
    print(ans)

if __name__ == '__main__':
    main()
