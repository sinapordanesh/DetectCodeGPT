def count_permutations(N, s):
    MOD = 10**9 + 7
    dp = [1] * (N + 1)
    for i in range(2, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    
    ans = 1
    for i in range(N - 1):
        if s[i] == "<":
            ans = (ans * (dp[i + 1] - dp[0])) % MOD
        else:
            ans = (ans * (dp[N] - dp[i + 1])) % MOD
    
    return ans

N = int(input())
s = input()
print(count_permutations(N, s))