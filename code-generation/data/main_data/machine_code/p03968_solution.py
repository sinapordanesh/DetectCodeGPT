def count_cubes(N, tiles):
    def rotate(tile):
        return [tile[3]] + tile[:3]

    def check_color(tile1, tile2):
        for i in range(4):
            if tile1[i] != tile2[i]:
                return False
        return True

    count = 0
    for i in range(N):
        for j in range(4):
            for k in range(i+1, N):
                for l in range(4):
                    for m in range(k+1, N):
                        for n in range(4):
                            colors = set()
                            colors.add(tiles[i][j])
                            colors.add(tiles[i][(j+1)%4])
                            colors.add(tiles[k][l])
                            colors.add(tiles[k][(l+1)%4])
                            colors.add(tiles[m][n])
                            colors.add(tiles[m][(n+1)%4])

                            if len(colors) == 1:
                                count += 1

    return count

# Input
N = 6
tiles = [
    [0, 1, 2, 3],
    [0, 4, 6, 1],
    [1, 6, 7, 2],
    [2, 7, 5, 3],
    [6, 4, 5, 7],
    [4, 0, 3, 5]
]

# Output
print(count_cubes(N, tiles))