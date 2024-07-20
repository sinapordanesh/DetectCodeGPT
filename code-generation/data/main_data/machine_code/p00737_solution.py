def twirling_robot(w, h, grid, costs):
    def dfs(x, y, cost):
        if x < 0 or x >= h or y < 0 or y >= w:
            return float('inf')
        command = grid[x][y]
        if command == 4:
            return 0
        new_cost = costs[command] + cost
        grid[x][y] = 4
        straight = dfs(x, y + 1, new_cost)
        right = dfs(x + 1, y, new_cost)
        back = dfs(x, y - 1, new_cost)
        left = dfs(x - 1, y, new_cost)
        grid[x][y] = command
        return min(straight, right, back, left)
    
    return dfs(0, 0, 0)