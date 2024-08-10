def place_tiles(N, M, A, B):
    if N*M % 2 != 0:
        print("NO")
        return

    if A % 2 == 1 and B % 2 == 1 and N % 2 == 1 and M % 2 == 1:
        print("NO")
        return

    grid = [['.' for _ in range(M)] for _ in range(N)]

    for i in range(0, N, 2):
        for j in range(0, M, 2):
            if A >= 2:
                grid[i][j] = '<'
                grid[i][j+1] = '>'
                A -= 2
            elif B >= 2:
                grid[i][j] = '^'
                grid[i+1][j] = 'v'
                B -= 2

    if A == 0 and B == 0:
        print("YES")
        for row in grid:
            print(''.join(row))
    else:
        print("NO")

# Sample Inputs
place_tiles(3, 4, 4, 2)
place_tiles(4, 5, 5, 3)
place_tiles(7, 9, 20, 20)