def magic_tile_movement():
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        room = [input() for _ in range(H)]
        visited = [[False] * W for _ in range(H)]
        x, y = 0, 0
        while True:
            if x < 0 or x >= W or y < 0 or y >= H:
                print("LOOP")
                break
            if visited[y][x]:
                print(x, y)
                break
            visited[y][x] = True
            if room[y][x] == '>':
                x += 1
            elif room[y][x] == '<':
                x -= 1
            elif room[y][x] == 'v':
                y += 1
            elif room[y][x] == '^':
                y -= 1
            else:
                print(x, y)
                break

magic_tile_movement()