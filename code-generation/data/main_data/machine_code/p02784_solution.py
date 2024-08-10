def can_win(H, N, moves):
    dp = [False] * (H + 1)
    dp[0] = True
    
    for i in range(1, H + 1):
        for move in moves:
            if i - move >= 0:
                dp[i] |= dp[i - move]
    
    return "Yes" if dp[H] else "No"