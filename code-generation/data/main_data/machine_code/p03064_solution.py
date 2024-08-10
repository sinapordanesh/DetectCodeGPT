def count_ways(N, arr):
    MOD = 998244353
    dp = [[0] * (sum(arr) + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(sum(arr) + 1):
            dp[i][j] = (2 * dp[i - 1][j] % MOD) % MOD
            if j >= arr[i - 1]:
                dp[i][j] += dp[i - 1][j - arr[i - 1]]
                dp[i][j] %= MOD
    ans = 0
    for j in range(sum(arr) + 1):
        if j < sum(arr) - j:
            ans += dp[N][j]
            ans %= MOD
    return ans

N = 4
arr = [1, 1, 1, 2]
print(count_ways(N, arr))

N = 6
arr = [1, 3, 2, 3, 5, 2]
print(count_ways(N, arr))

N = 20
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
print(count_ways(N, arr))