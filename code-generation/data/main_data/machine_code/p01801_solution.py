def wall_making_game(H, W, board):
    def dfs(x, y):
        if x < 0 or x >= H or y < 0 or y >= W or board[x][y] != '.':
            return
        board[x][y] = '#'
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                dfs(i, j)
                return "First"
    
    return "Second"