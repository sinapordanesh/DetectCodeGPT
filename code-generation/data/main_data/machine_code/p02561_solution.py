def max_tiles_placement(N, M, grid):
    max_tiles = 0
    result = []
    
    for i in range(N):
        row = list(grid[i])
        for j in range(0, M, 2):
            if j+1 < M and row[j] == '.' and row[j+1] == '.':
                max_tiles += 1
                row[j], row[j+1] = '>', '<'
        
        result.append(''.join(row))
    
    return max_tiles, result

# Sample Input
N = 3
M = 3
grid = ["#..", "..#", "..."]

max_tiles, result = max_tiles_placement(N, M, grid)
for res in result:
    print(res)