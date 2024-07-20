def num_ways_to_bottom_right(H, W, A, B):
    MOD = 10**9 + 7
    dp = [[0] * (W-B) for _ in range(H-A)]
    dp[0][0] = 1
    
    for i in range(H-A):
        for j in range(W-B):
            if i+1 < H-A:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD
            if j+1 < W-B:
                dp[i][j+1] += dp[i][j]
                dp[i][j+1] %= MOD
    
    return dp[-1][-1]

# Sample Input 1
print(num_ways_to_bottom_right(2,3,1,1))

# Sample Input 2
print(num_ways_to_bottom_right(10,7,3,4))

# Sample Input 3
print(num_ways_to_bottom_right(100000,100000,99999,99999))

# Sample Input 4
print(num_ways_to_bottom_right(100000,100000,44444,55555))