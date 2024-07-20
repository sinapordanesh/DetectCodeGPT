def separate_string(N, S, t):
    MOD = 1000000007
    
    dp = [0] * (len(t)+1)
    dp[0] = 1
    
    for i in range(1, len(t)+1):
        for s in S:
            if i >= len(s) and t[i-len(s):i] == s:
                dp[i] += dp[i-len(s)]
                dp[i] %= MOD
    
    return dp[-1]

# Sample Input 1
print(separate_string(3, ['a', 'b', 'ab'], 'abab'))

# Sample Input 2
print(separate_string(3, ['a', 'b', 'c'], 'xyz'))

# Sample Input 3
print(separate_string(7, ['abc', 'ab', 'bc', 'a', 'b', 'c', 'aa'], 'aaabcbccababbc'))

# Sample Input 4
print(separate_string(10, ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa'], 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))