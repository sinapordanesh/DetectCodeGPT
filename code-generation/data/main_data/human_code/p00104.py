
dir = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}

# solve function
def solve(h, w, tiles, visited):
     x, y = 0, 0

     while True:
         if tiles[y][x] == '.':
             print(x, y)
             break

         if not visited[y][x]:
             print("LOOP")
             break

         visited[y][x] = False

         next_y, next_x = dir[tiles[y][x]]

         x += next_x
         y += next_y

     return

# main function
if __name__ == '__main__':
    while True:
        # input param
        inputs = (input()).split()

        h = int(inputs[0])
        w = int(inputs[1])

        if h == 0 and w == 0:
            break

        visited = [[True for i in range(w)] for j in range(h)]
        tiles = ["" for i in range(h)]

        for i in range(h):
            tiles[i] = input()

        solve(h, w, tiles, visited)