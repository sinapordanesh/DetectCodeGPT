def frog_race(N, robots):
    mod = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1

    for i in range(1, N+1):
        for j in range(i):
            if robots[i-1] - robots[j] >= 2:
                dp[i] = (dp[i] + dp[j]) % mod

    return dp[N]

# Sample Input 1
print(frog_race(3, [1, 2, 3]))

# Sample Input 2
print(frog_race(3, [2, 3, 4]))

# Sample Input 3
print(frog_race(8, [1, 2, 3, 5, 7, 11, 13, 17]))

# Sample Input 4
print(frog_race(13, [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]))