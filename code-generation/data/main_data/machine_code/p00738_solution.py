def find_largest_radius():
    while True:
        N = int(input())
        if N == 0:
            break
        sx, sy, ex, ey = map(int, input().split())
        obstacles = []
        for _ in range(N):
            minx, miny, maxx, maxy, h = map(int, input().split())
            obstacles.append((minx, miny, maxx, maxy, h))

        def check_collision(x, y, r):
            for obstacle in obstacles:
                minx, miny, maxx, maxy, h = obstacle
                if x + r >= minx and x - r <= maxx and y + r >= miny and y - r <= maxy:
                    if h < r:
                        return True
                    height_diff = h - r
                    if x + r >= minx and x - r <= maxx and y + r >= miny and y - r <= maxy:
                        return True
                    if x + r >= minx and x - r <= maxx and y + r >= maxy and y - r < maxy:
                        if y < maxy:
                            if (r ** 2 - (maxy - y) ** 2) ** 0.5 >= min(height_diff, maxy - y):
                                return True
                        else:
                            if r >= height_diff:
                                return True
                    if x + r >= maxx and x - r < maxx and y + r >= miny and y - r <= maxy:
                        if x < maxx:
                            if (r ** 2 - (maxx - x) ** 2) ** 0.5 >= min(height_diff, maxx - x):
                                return True
                        else:
                            if r >= height_diff:
                                return True
                    if x + r >= minx and x - r <= minx and y + r >= miny and y - r <= maxy:
                        if x > minx:
                            if (r ** 2 - (x - minx) ** 2) ** 0.5 >= min(height_diff, x - minx):
                                return True
                        else:
                            if r >= height_diff:
                                return True
                    if x + r >= minx and x - r <= maxx and y + r >= miny and y - r < miny:
                        if y > miny:
                            if (r ** 2 - (y - miny) ** 2) ** 0.5 >= min(height_diff, y - miny):
                                return True
                        else:
                            if r >= height_diff:
                                return True
            return False

        def calculate_distance(x, y):
            return ((x - sx) ** 2 + (y - sy) ** 2) ** 0.5

        l, r = 0, calculate_distance(ex, ey)
        while r - l > 0.001:
            m = (l + r) / 2
            if check_collision(ex, ey, m):
                r = m
            else:
                l = m
        print("{:.10f}".format(l))

find_largest_radius()