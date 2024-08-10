def main():
    mod = 998244353
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [0] * (s + 1)

    for i, x in enumerate(a):
        if x >= s:
            if x == s:
                dp[s] += (i + 1) * (n - i)
                dp[s] %= mod
            continue

        dp[s] += dp[s-x] * (n - i)
        dp[s] %= mod

        for j in range(s-x-1, 0, -1):
            dp[j+x] += dp[j]
            dp[j+x] %= mod

        dp[x] += i + 1
        dp[x] %= mod

    print(dp[s])

main()