anslist = []
def sarch(i, j, visited):

    if 0 < i:
        if visited[i - 1][j] == 0:
            visited[i - 1][j] = 1
            sarch(i - 1, j, visited)
    if i < len(visited) - 1:
        if visited[i + 1][j] == 0:
            visited[i + 1][j] = 1
            sarch(i + 1, j, visited)
    if 0 < j:
        if visited[i][j - 1] == 0:
            visited[i][j - 1] = 1
            sarch(i, j - 1, visited)
    if j < len(visited[0]) - 1:
        if visited[i][j + 1] == 0:
            visited[i][j + 1] = 1
            sarch(i, j + 1, visited)
    return visited


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = [list(input()) for i in range(h)]
    visited = [[0 for i in range(w)] for j in range(h)]
    starti = 0
    startj = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "@":
                starti = i
                startj = j
                visited[i][j] = 1
            elif grid[i][j] == "#":
                visited[i][j] = -1
            else:
                visited[i][j] = 0

    visited = sarch(starti, startj, visited)
    #print(visited)
    ans = 0
    for i in visited:
        for j in i:
            if j == 1:
                ans += 1
    anslist.append(ans)

for i in anslist:
    print(i)
