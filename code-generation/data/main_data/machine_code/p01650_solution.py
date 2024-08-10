def jewels_and_holes(H, W, grid):
    def dfs(i, j, jewels_collected, visited):
        if i < 0 or i >= H or j < 0 or j >= W or grid[i][j] == '#' or visited[i][j]:
            return 0
        
        visited[i][j] = True
        
        if grid[i][j].islower():
            jewels_collected.append(grid[i][j])
        
        if i == H - 1 and j == W - 1:
            return len(jewels_collected)
        
        right = dfs(i, j + 1, jewels_collected[:], visited)
        down = dfs(i + 1, j, jewels_collected[:], visited)
        
        return max(right, down)
    
    visited = [[False for _ in range(W)] for _ in range(H)]
    result = dfs(0, 0, [], visited)
    
    return result


datasets = [[3, 3, ['ac#', 'b#C', '.BA']],
            [3, 3, ['aaZ', 'a#Z', 'aZZ']],
            [3, 3, ['..#', '.#.', '#..']],
            [1, 50, ['abcdefghijklmnopqrstuvwxyYXWVUTSRQPONMLKJIHGFEDCBA']],
            [1, 50, ['aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyY']],
            [1, 50, ['abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY']],
            [1, 50, ['aaaaaaaaaabbbbbbbbbbcccccCCCCCBBBBBBBBBBAAAAAAAAAA']],
            [10, 10, ['...#......', 'a###.#####', '.bc...A...', '##.#C#d#.', '.#B#.#.###', '.#...#e.D.', '.#A..###.#', '..e.c#..E.', '####d###.#', '##E...D.C.']]]


for data in datasets:
    print(jewels_and_holes(data[0], data[1], data[2]))