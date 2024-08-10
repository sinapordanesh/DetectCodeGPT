def max_score():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    visited = [[False]*W for _ in range(H)]
    queue = [(0, 0, 0)]
    
    while queue:
        i, j, score = queue.pop(0)
        if i == H-1 and j == W-1:
            return score
        if visited[i][j]:
            continue
        visited[i][j] = True
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and grid[ni][nj] != '#':
                queue.append((ni, nj, score + 1))
    
    return -1

print(max_score())