import math

def area_of_intersection():
    n, r = map(int, input().split())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    def dist(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def segment_area(p1, p2, r):
        theta = math.acos((2*r**2 - dist(p1, p2)**2) / (2*r**2))
        return (theta - math.sin(theta)) * r**2 / 2
    
    total_area = 0
    for i in range(n):
        total_area += segment_area(points[i], points[(i+1)%n], r)
    
    print(round(total_area, 10))

area_of_intersection()