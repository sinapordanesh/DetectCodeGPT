def circle_and_points():
    while True:
        n = int(input())
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y = map(float, input().split())
            points.append((x, y))
        max_enclosed = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cnt = 2
                for k in range(n):
                    if k != i and k != j:
                        x3, y3 = points[k]
                        if (x1-x2)**2 + (y1-y2)**2 + (x2-x3)**2 + (y2-y3)**2 <= 8:
                            cnt += 1
                max_enclosed = max(max_enclosed, cnt)
        print(max_enclosed)