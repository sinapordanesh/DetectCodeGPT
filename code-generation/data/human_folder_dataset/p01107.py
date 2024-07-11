dd = [(-1, 0), (0, -1), (1, 0), (0, 1)]
while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    C = [list(input() + "#") for i in range(n)] + ["#"*(m+2)]

    used = [[0]*m for i in range(n)]
    def move(x0, y0, x1, y1, d):
        x = x0; y = y0
        moved = 0; cnt = 0
        history = []
        while x != x1 or y != y1:
            cnt += 1
            rx, ry = dd[d-3]
            dx, dy = dd[d]
            while C[y+dy][x+dx] != '#' and C[y+ry][x+rx] == '#':
                x += dx; y += dy
                history.append([x, y])
                moved = 1
            if C[y+dy][x+dx] == '#' and C[y+ry][x+rx] == '#':
                d = (d - 1) % 4
            elif C[y+ry][x+rx] != '#':
                d = (d + 1) % 4
                x += rx; y += ry
                history.append([x, y])
            if (moved or cnt > 4) and x == x0 and y == y0:
                return 0
        for x, y in history[:-1]:
            C[y][x] = '#'
        return 1
    if move(0, 0, 0, n-1, 3) and move(0, n-1, m-1, n-1, 2) and move(m-1, n-1, m-1, 0, 1) and move(m-1, 0, 0, 0, 0):
        print("YES")
    else:
        print("NO")