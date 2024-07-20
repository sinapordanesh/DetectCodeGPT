def max_operations(N, M, board):
    def dfs(i, j):
        if i < 0 or i >= N or j < 0 or j >= M or visited[i][j] or board[i][j] == '#':
            return 0
        visited[i][j] = True
        res = 0
        for dx, dy in [(1, 0), (0, 1)]:
            x, y = i + dx, j + dy
            if x < 0 or x >= N or y < 0 or y >= M or board[x][y] == '#':
                continue
            res = max(res, dfs(x, y))
        visited[i][j] = False
        return res + 1

    visited = [[False for _ in range(M)] for _ in range(N)]
    max_ops = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                max_ops = max(max_ops, dfs(i, j) - 1)
    return max_ops

N, M = 3, 3
board = ['o..', '...', 'o.#']
print(max_operations(N, M, board))

N, M = 9, 10
board = ['.#....o#..', '.#..#..##o', '.....#o.##', '.###.#o..o', '#.#...##.#', '..#..#.###', '#o.....#..', '....###..o', 'o.......o#']
print(max_operations(N, M, board))