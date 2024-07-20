def cleaning_robot(arr):
    def bfs(i, j, visited):
        queue = []
        visited[i][j] = 0
        queue.append((i, j))

        while queue:
            x, y = queue.pop(0)

            for k in range(4):
                new_x = x + dx[k]
                new_y = y + dy[k]

                if 0 <= new_x < h and 0 <= new_y < w and visited[new_x][new_y] == -1 and arr[new_x][new_y] != 'x':
                    visited[new_x][new_y] = visited[x][y] + 1
                    queue.append((new_x, new_y))


    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        arr = [input() for _ in range(h)]
        dirty_tiles = 0

        for i in range(h):
            for j in range(w):
                if arr[i][j] == 'o':
                    start_x, start_y = i, j
                if arr[i][j] == '*':
                    dirty_tiles += 1

        visited = [[-1] * w for _ in range(h)]
        bfs(start_x, start_y, visited)

        total_moves = sum(1 for i in visited for j in i if j != -1)
        if total_moves == dirty_tiles:
            print(total_moves)
        else:
            print(-1)