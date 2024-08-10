from decimal import Decimal

def area_of_polygon():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    area = 0
    for i in range(n):
        area += (points[i][0] * points[(i+1)%n][1]) - (points[(i+1)%n][0] * points[i][1])
    
    area = abs(area) / 2
    print(round(Decimal(area), 1))

area_of_polygon()