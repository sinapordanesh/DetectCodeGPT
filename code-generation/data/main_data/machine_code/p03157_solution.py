def count_pairs_of_black_and_white_squares(H, W, grid):
    def dfs(i, j, color):
        if i < 0 or i >= H or j < 0 or j >= W or visited[i][j] or grid[i][j] != color:
            return
        visited[i][j] = True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + dx, j + dy
            dfs(new_i, new_j, color ^ 1)
            
    grid = [list(row) for row in grid]
    visited = [[False for _ in range(W)] for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j]:
                dfs(i, j, 0)
                black_count = sum(row.count('#') for row in visited)
                white_count = sum(row.count('.') for row in visited)
                count += black_count * white_count
    return count

# Sample Input
print(count_pairs_of_black_and_white_squares(3, 3, ["#.","..","#.."])) # Output: 10
print(count_pairs_of_black_and_white_squares(2, 4, ["....","...."])) # Output: 0
print(count_pairs_of_black_and_white_squares(4, 3, ["###","###","...","###"])) # Output: 6