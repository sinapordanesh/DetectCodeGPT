def abc129c():
    n, m = map(int, input().split())
    set_a = set()
    for _ in range(m):
        set_a.add(int(input()))
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i in set_a: continue
        dp[i] = dp[i-1]
        if i > 1:
            dp[i] += dp[i-2]
    print(dp[n]%1000000007)
abc129c()