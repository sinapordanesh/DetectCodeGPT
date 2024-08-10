def pablo_squarson_headache():
    while True:
        N = int(input())
        if N == 0:
            break
        x, y, dx, dy = 0, 0, 1, 0
        for _ in range(N-1):
            n, d = map(int, input().split())
            if d == 0:
                dx, dy = -dy, dx
            elif d == 1:
                dx, dy = dx, -dy
            elif d == 2:
                dx, dy = dy, -dx
            x, y = x + dx, y + dy
        print(abs(x) + 1, abs(y) + 1)