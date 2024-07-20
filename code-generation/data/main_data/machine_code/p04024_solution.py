def fractal_connected_components(H, W, K, grid):
    MOD = 10**9 + 7

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c, level):
        if visited[level][r][c]:
            return
        visited[level][r][c] = True
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H * (2 ** level) and 0 <= nc < W * (2 ** level) and grid[nr // (2 ** level)][nc // (2 ** level)] == '#':
                dfs(nr, nc, level)

    visited = [[[False for _ in range(W * (2 ** K))] for _ in range(H * (2 ** K))] for _ in range(K + 1)]

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                dfs(i, j, 0)

    for level in range(1, K + 1):
        for i in range(H * (2 ** level)):
            for j in range(W * (2 ** level)):
                if grid[i // (2 ** level)][j // (2 ** level)] == '.':
                    visited[level][i][j] = True

                if not visited[level][i][j]:
                    dfs(i, j, level)

    count = sum(1 for i in range(H * (2 ** K)) for j in range(W * (2 ** K)) if visited[K][i][j]) % MOD
    return count

# Sample Input 1
print(fractal_connected_components(3, 3, 3, [".#.", "###", "#.#"]))

# Sample Input 2
print(fractal_connected_components(3, 3, 3, ["###", "#.#", "###"]))

# Sample Input 3
print(fractal_connected_components(11, 15, 1000000000000000000, [".....#.........",
                                                                  "....###........",
                                                                  "....####.......",
                                                                  "...######......",
                                                                  "...#######.....",
                                                                  "..##.###.##....",
                                                                  "..##########...",
                                                                  ".###.....####..",
                                                                  ".####...######.",
                                                                  "###############",
                                                                  "#.##..##..##..#"]))