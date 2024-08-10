def find_point():
    while True:
        n = int(input())
        if n == 0:
            break
        
        points = []
        for _ in range(n):
            x1, y1, x2, y2 = map(int, input().split())
            points.append(((x1 + x2) / 2, (y1 + y2) / 2))
        
        unique_points = set(points)
        
        if len(unique_points) == 1:
            print(f"{unique_points.pop()[0]:.4f} {unique_points.pop()[1]:.4f}")
        elif len(unique_points) == n:
            print("Many")
        else:
            print("None")