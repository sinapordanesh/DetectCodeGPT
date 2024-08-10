def maximum_cargo_capacity():
    H, N = map(int, input().split())
    grid = [[1 for _ in range(H)] for _ in range(4)]
    for _ in range(N):
        x, y = map(int, input().split())
        grid[x][y] = 0
    count = 0
    for i in range(4):
        for j in range(H):
            if grid[i][j] == 1:
                count += 1
    print(count)

maximum_cargo_capacity()