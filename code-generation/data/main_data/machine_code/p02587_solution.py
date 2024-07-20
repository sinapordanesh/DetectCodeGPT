def min_total_cost_to_make_palindrome(N, strings):
    dp = {0: 0}
    for i in range(1, 1<<N):
        dp[i] = float('inf')
        s = ''
        cost = 0
        for j in range(N):
            if i & (1<<j):
                s += strings[j][0]
                cost += strings[j][1]
        if s == s[::-1]:
            dp[i] = min(dp[i], cost)
        for j in range(i):
            if (i & j) == j:
                dp[i] = min(dp[i], dp[j] + dp[i-j])
    return dp[(1<<N)-1] if dp[(1<<N)-1] != float('inf') else -1

# Input
N = 3
strings = [('ba', 3), ('abc', 4), ('cbaa', 5)]

# Function Call
print(min_total_cost_to_make_palindrome(N, strings))