def chain_disappearance_puzzle():
    while True:
        H = int(input())
        if H == 0:
            break
        board = [list(map(int, input().split())) for _ in range(H)]
        
        def check_disappearances(board):
            rows, cols = len(board), len(board[0])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            visited = [[False] * cols for _ in range(rows)]
            
            def dfs(row, col, digit):
                nonlocal visited
                if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or board[row][col] != digit:
                    return 0
                visited[row][col] = True
                count = 1
                for dr, dc in directions:
                    count += dfs(row + dr, col + dc, digit)
                return count
            
            total_score = 0
            for i in range(rows):
                for j in range(cols):
                    if not visited[i][j]:
                        disappear_count = dfs(i, j, board[i][j])
                        if disappear_count >= 3:
                            total_score += disappear_count * board[i][j]
            return total_score
        
        print(check_disappearances(board))

chain_disappearance_puzzle()