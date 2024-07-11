import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L = list(input())
    n = len(L)

    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        if L[i - 1] == "0":
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = (dp[i - 1][1] * 3) % mod
        else:
            dp[i][0] = (dp[i - 1][0] * 2) % mod
            dp[i][1] = (dp[i - 1][1] * 3 + dp[i - 1][0]) % mod

    print((dp[-1][0] + dp[-1][1]) % mod)


if __name__ == '__main__':
    resolve()
