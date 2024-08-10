def min_moves_needed(H, W, cells):
    dp = [[float('inf') for _ in range(W+1)] for _ in range(H+1)]
    dp[0][1] = 0

    for i in range(1, H+1):
        left_blocked = 0
        for j in range(1, W+1):
            if j in cells[i-1]:
                left_blocked = j
            dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1 if left_blocked < j else float('inf'))

    result = []
    for i in range(1, H+1):
        if min(dp[i]) == float('inf'):
            result.append(-1)
        else:
            result.append(min(dp[i]))

    return result

# Sample Input
H = 4
W = 4
cells = [[2, 4], [1, 1], [2, 3], [2, 4]]

print(min_moves_needed(H, W, cells))