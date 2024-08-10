def count_strings(N):
    mod = 998244353
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = (dp[i - 1] * 3) % mod
    ans = dp[N]
    for i in range(1, N // 2 + 1):
        add = (dp[i - 1] * dp[N - 2 * i]) % mod
        add = (add * 2) % mod
        ans = (ans + add) % mod
    return ans

N = int(input().strip())
print(count_strings(N))