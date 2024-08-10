def is_objective_achievable(s, x, y):
    def dfs(i, j, dx, dy):
        if (i, j) == (x, y):
            return True
        if i + j > len(s) or (i, j) in visited:
            return False
        visited.add((i, j))
        if dfs(i + 1, j, dx, dy) or dfs(i, j + 1, dx, dy):
            return True
        if dfs(i + 1, j, -dy, dx) or dfs(i, j + 1, dy, -dx):
            return True
        return False

    visited = set()
    return "Yes" if dfs(0, 0, 0, 1) else "No"