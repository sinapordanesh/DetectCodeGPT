import math

def disk_intersection_area(n, r, vertices):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    
    def dist(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    def sector_area(angle, r):
        return 0.5 * r ** 2 * angle
    
    def intersection_area(r, a, b, c):
        angle_a = 2 * math.acos((a ** 2 + r ** 2 - b ** 2) / (2 * a * r))
        angle_b = 2 * math.acos((b ** 2 + r ** 2 - c ** 2) / (2 * b * r))
        return sector_area(angle_a, r) + sector_area(angle_b, r)

    total_area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        a = dist(x1, y1, x2, y2)
        b = dist(0, 0, x1, y1)
        c = dist(0, 0, x2, y2)
        total_area += area(0, 0, x1, y1, x2, y2) + intersection_area(r, a, b, c)
    
    return total_area

# Sample Input
print(disk_intersection_area(4, 4, [(0, 0), (6, 0), (6, 6), (0, 6)]))
print(disk_intersection_area(3, 1, [(0, 0), (2, 1), (1, 3)]))
print(disk_intersection_area(3, 1, [(0, 0), (100, 1), (99, 1)]))
print(disk_intersection_area(4, 1, [(0, 0), (100, 10), (100, 12), (0, 1)]))
print(disk_intersection_area(10, 10, [(0, 0), (10, 0), (20, 1), (30, 3), (40, 6), (50, 10), (60, 15), (70, 21), (80, 28), (90, 36)]))
print(disk_intersection_area(10, 49, [(50, 0), (79, 10), (96, 32), (96, 68), (79, 90), (50, 100), (21, 90), (4, 68), (4, 32), (21, 10)]))