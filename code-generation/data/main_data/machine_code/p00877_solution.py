def separate_points():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        points = []
        for _ in range(n + m):
            x, y = map(int, input().split())
            points.append((x, y))
        
        black_points = points[:n]
        white_points = points[n:]
        
        for i in range(len(black_points)):
            for j in range(len(white_points)):
                x1, y1 = black_points[i]
                x2, y2 = white_points[j]
                count = 0
                for k in range(len(points)):
                    x3, y3 = points[k]
                    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
                        count += 1
                if count == len(points):
                    print("YES")
                    break
            else:
                continue
            break
        else:
            print("NO")

separate_points()