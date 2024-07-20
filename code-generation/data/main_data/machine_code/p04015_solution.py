def ways_to_select_cards(N, A, cards):
    dp = [[[0]*2501 for _ in range(51)] for _ in range(51)]
    dp[0][0][0] = 1
    
    for i in range(N):
        for j in range(N, 0, -1):
            for k in range(2500):
                if k-cards[i] >= 0:
                    dp[i+1][j][k] += dp[i][j][k-cards[i]]
            for k in range(1, 2501):
                dp[i+1][j][k] += dp[i][j-1][k]
    
    ans = 0
    for j in range(1, N+1):
        ans += dp[N][j][j*A]
    
    return ans

# Sample Input 1
print(ways_to_select_cards(4, 8, [7, 9, 8, 9]))

# Sample Input 2
print(ways_to_select_cards(3, 8, [6, 6, 9]))

# Sample Input 3
print(ways_to_select_cards(8, 5, [3, 6, 2, 8, 7, 6, 5, 9]))

# Sample Input 4
print(ways_to_select_cards(33, 3, [3]*33))