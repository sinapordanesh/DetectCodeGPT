def largest_square_area(matrix):
    H, W = len(matrix), len(matrix[0])
    dp = [[0] * W for _ in range(H)]
    max_side = 0
    
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == 0:
                dp[i][j] = 1
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                max_side = max(max_side, dp[i][j])
    
    return max_side ** 2

# Sample Input
matrix = [
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

print(largest_square_area(matrix))