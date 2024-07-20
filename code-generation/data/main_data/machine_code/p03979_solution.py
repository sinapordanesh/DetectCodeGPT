def min_fences_needed(H, W, grid):
    
    def is_valid(i, j):
        return 0 <= i < H and 0 <= j < W
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    fences = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "X":
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if not is_valid(ni, nj) or grid[ni][nj] == ".":
                        fences += 1
    
    return fences

# Input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Output
print(min_fences_needed(H, W, grid))