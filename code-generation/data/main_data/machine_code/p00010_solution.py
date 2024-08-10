def circumscribed_circle_triangle():
    import math

    n = int(input())
    
    for _ in range(n):
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        
        D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        
        px = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / D
        py = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / D
        r = math.sqrt((x1 - px)**2 + (y1 - py)**2)
        
        print(f'{px:.3f} {py:.3f} {r:.3f}')