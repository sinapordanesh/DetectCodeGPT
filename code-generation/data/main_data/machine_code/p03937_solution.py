def possible_moves(H, W, matrix):
    def dfs(i, j):
        if i == H-1 and j == W-1:
            return True
        if i < H-1 and matrix[i+1][j] == "#":
            if dfs(i+1, j):
                return True
        if j < W-1 and matrix[i][j+1] == "#":
            if dfs(i, j+1):
                return True
        return False

    if dfs(0, 0):
        return "Possible"
    else:
        return "Impossible"