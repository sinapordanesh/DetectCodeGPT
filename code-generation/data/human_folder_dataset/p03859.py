#!/usr/bin/env python3


M = 10 ** 9 + 7


def solve(n, m, s, lst):

    cnt = [0] * n
    t = 0
    for i in range(n):
        if s[i] == '1':
            t += 1
        cnt[i] = t


    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    r = 0
    j = 0
    for i in range(n):
        while j < m:
            lj, rj = lst[j]
            if lj <= i:
                r = max(r, rj)
                j += 1
            else:
                break
        if r <= i:
            c = cnt[i]
            if 0 < c:
                dp[i + 1][cnt[i]] = (dp[i][c] + dp[i][c - 1]) % M
            else:
                dp[i + 1][0] = dp[i][0]
        else:
            for k in range(max(0, cnt[r] - r + i), min(i + 1, cnt[r]) + 1):
                if 0 < k:
                    dp[i + 1][k] = (dp[i][k] + dp[i][k - 1]) % M
                else:
                    dp[i + 1][0] = dp[i][0]

    return dp[n][cnt[n - 1]]


def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    s = input()
    lst = []
    for _ in range(m):
        l, r = input().split()
        l = int(l) - 1
        r = int(r) - 1
        lst.append((l, r))

    print(solve(n, m, s, lst))


if __name__ == '__main__':
    main()

