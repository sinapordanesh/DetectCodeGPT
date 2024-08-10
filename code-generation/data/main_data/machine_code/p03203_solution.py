def takahashi_actions():
    H, W, N = map(int, input().split())
    obstacles = set()
    for _ in range(N):
        x, y = map(int, input().split())
        obstacles.add((x, y))
    
    actions = 0
    x, y = 1, 1
    while True:
        if (x, y) in obstacles:
            break
        if x == H and y == W:
            break
        if x + y > 2:
            actions += 1
        if (x+1, y) in obstacles and (x, y+1) in obstacles:
            break
        if (x+1, y) in obstacles or y == W:
            x += 1
        elif (x, y+1) in obstacles or x == H:
            y += 1
        else:
            if x + 1 + y > x + y + 1:
                x += 1
            else:
                y += 1
    print(actions)

takahashi_actions()