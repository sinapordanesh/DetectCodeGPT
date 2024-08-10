def count_painted_grids(H, W, grid):
    MOD = 998244353
    ans = 1
    for i in range(H):
        black_count = grid[i].count('#')
        ans *= pow(2, W - black_count, MOD)
        ans %= MOD
    for j in range(W):
        black_count = sum(1 for i in range(H) if grid[i][j] == '#')
        ans *= pow(2, H - black_count, MOD)
        ans %= MOD
    return ans

# Sample Input
print(count_painted_grids(2, 2, ['#.', '.#']))
print(count_painted_grids(3, 3, ['...', '...', '...']))
print(count_painted_grids(2, 4, ['#...', '...#']))
print(count_painted_grids(6, 7, ['.......', '.......', '.#.....', '..#....', '.#.#...', '.......']))