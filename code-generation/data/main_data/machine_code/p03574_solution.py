def bomb_adjacent(H, W, grid):
    def count_adjacent_bombs(i, j):
        count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if 0 <= x < H and 0 <= y < W and grid[x][y] == '#':
                    count += 1
        return str(count)
    
    result = []
    for i in range(H):
        row = []
        for j in range(W):
            if grid[i][j] == '.':
                row.append(count_adjacent_bombs(i, j))
            else:
                row.append('#')
        result.append(''.join(row))
    
    return result

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
output = bomb_adjacent(H, W, grid)
for line in output:
    print(line)