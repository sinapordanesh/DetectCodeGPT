def help_the_princess():
    H, W = map(int, input().split())
    palace = [input() for _ in range(H)]

    def dfs(x, y):
        if not (0 <= x < H and 0 <= y < W) or palace[x][y] == '#' or visited[x][y]:
            return False
        if palace[x][y] == '%':
            return True

        visited[x][y] = True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if dfs(x + dx, y + dy):
                return True
        return False

    visited = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if palace[i][j] == '@':
                if dfs(i, j):
                    print("Yes")
                    return
    print("No")

help_the_princess()