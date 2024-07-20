import bisect

INF = 1 << 30


def main():
    n = int(input())
    a = [int(input()) for i in range(n)]

    dp = [INF for i in range(n+1)]
    for i in range(1, n+1):
        idx = bisect.bisect_left(dp, a[i-1])
        dp[idx] = a[i-1]

    ans = bisect.bisect_left(dp, INF)
    print(ans)


if __name__ == '__main__':
    main()

