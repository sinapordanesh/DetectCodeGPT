import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 998244353


def resolve():
    a, b, c, d = map(int, input().split())
    dp = [[0] * (d + 1) for _ in range(c + 1)]
    dp[a][b] = 1
    for i in range(a, c + 1):
        for j in range(b, d + 1):
            if i == a and j == b:
                continue
            dp[i][j] = dp[i - 1][j] * j + dp[i][j - 1] * i - dp[i - 1][j - 1] * (i - 1) * (j - 1)
            dp[i][j] %= mod

    print(dp[-1][-1] % mod)


if __name__ == '__main__':
    resolve()
