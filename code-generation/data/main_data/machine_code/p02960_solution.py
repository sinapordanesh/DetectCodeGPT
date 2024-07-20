MOD = 10**9 + 7

def count_strings_with_remainder(s):
    dp = [[0] * 13 for _ in range(len(s) + 1)]
    dp[0][0] = 1

    for i in range(len(s)):
        for j in range(13):
            for d in range(10):
                if s[i] != '?' and int(s[i]) != d:
                    continue
                next_mod = (j * 10 + d) % 13
                dp[i+1][next_mod] += dp[i][j]
                dp[i+1][next_mod] %= MOD

    return dp[len(s)][5]

# Driver code
S = input()
print(count_strings_with_remainder(S))