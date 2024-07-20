def possible_final_sequences_of_colors(N, colors):
    MOD = 10**9 + 7
    last_pos = {}
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i, color in enumerate(colors, 1):
        if color in last_pos:
            dp[i] = (dp[i] + dp[last_pos[color]]) % MOD
        last_pos[color] = i
    
    return dp[N]

# Sample Input 1
print(possible_final_sequences_of_colors(5, [1, 2, 1, 2, 2]))

# Sample Input 2
print(possible_final_sequences_of_colors(6, [4, 2, 5, 4, 2, 4]))

# Sample Input 3
print(possible_final_sequences_of_colors(7, [1, 3, 1, 2, 3, 3, 2]))