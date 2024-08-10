def count_black_tiles(W, H, tiles):
    def dfs(x, y):
        nonlocal count
        if x < 0 or x >= H or y < 0 or y >= W or tiles[x][y] != '.':
            return
        count += 1
        tiles[x][y] = '#'
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
    
    count = 0
    for i in range(H):
        for j in range(W):
            if tiles[i][j] == '@':
                dfs(i, j)
                return count

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    tiles = [list(input()) for _ in range(H)]
    print(count_black_tiles(W, H, tiles))