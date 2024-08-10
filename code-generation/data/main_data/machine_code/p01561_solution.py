def escape_labyrinth():
    W, H = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    S = int(input())
    switches = [list(input()) for _ in range(S)]

    def find_start_and_end():
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '%':
                    start = (i, j, 0)  # (row, col, floor)
                elif grid[i][j] == '&':
                    end = (i, j)
        return start, end

    start, end = find_start_and_end()

    def is_valid_move(row, col, floor):
        return 0 <= row < H and 0 <= col < W and grid[row][col] != '#'

    def bfs():
        queue = [start]
        visited = set([start])
        steps = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            size = len(queue)
            for _ in range(size):
                row, col, floor = queue.pop(0)

                if grid[row][col].islower() and switches[ord(grid[row][col]) - ord('a')][floor] == '*':
                    floor = 1 - floor  # switch the floor

                if (row, col) == end:
                    return steps
                
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if is_valid_move(new_row, new_col, floor) and (new_row, new_col, floor) not in visited:
                        queue.append((new_row, new_col, floor))
                        visited.add((new_row, new_col, floor))
            
            steps += 1

        return -1

    print(bfs())

escape_labyrinth()