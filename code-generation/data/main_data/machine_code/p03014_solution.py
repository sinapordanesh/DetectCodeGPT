def max_lighted_squares(H, W, grid):
    max_count = 0
    for i in range(H):
        for j in range(W):
            count = 1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i, j
                while 0 <= ni+di < H and 0 <= nj+dj < W and grid[ni+di][nj+dj] != "#":
                    count += 1
                    ni += di
                    nj += dj
            max_count = max(max_count, count)
    return max_count


# Sample Input 1
print(max_lighted_squares(4, 6, ['#..#..', '.....#', '....#.', '#.#...']))

# Sample Input 2
print(max_lighted_squares(8, 8, ['..#...#.', '....#...', '##......', '..###..#', '...#..#.', '##....#.', '#...#...', '###.#..#']))