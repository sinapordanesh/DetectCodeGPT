def count_islands(w, h, map_data):
    def dfs(i, j):
        if i < 0 or i >= h or j < 0 or j >= w or map_data[i][j] == 0:
            return
        map_data[i][j] = 0
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j+1)
        dfs(i+1, j-1)
        dfs(i-1, j+1)
        dfs(i-1, j-1)

    islands = 0
    for i in range(h):
        for j in range(w):
            if map_data[i][j] == 1:
                islands += 1
                dfs(i, j)

    return islands

# Read input
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    map_data = []
    for _ in range(h):
        row = list(map(int, input().split()))
        map_data.append(row)
    islands = count_islands(w, h, map_data)
    print(islands)