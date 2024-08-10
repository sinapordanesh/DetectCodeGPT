def max_souvenirs(H, W, grid):
    def dfs(i, j, player):
        if i == H-1 and j == W-1:
            return grid[i][j]
        
        if player == "Sigma":
            next_player = "Sugim"
            next_sum = 0
            for dx, dy in [(1, 0), (0, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < H and 0 <= y < W:
                    next_sum = max(next_sum, grid[i][j] + dfs(x, y, next_player))
            return next_sum
        else:
            next_player = "Sigma"
            next_sum = float('-inf')
            for dx, dy in [(1, 0), (0, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < H and 0 <= y < W:
                    next_sum = max(next_sum, grid[i][j] + dfs(x, y, next_player))
            return next_sum
    
    return dfs(0, 0, "Sigma")