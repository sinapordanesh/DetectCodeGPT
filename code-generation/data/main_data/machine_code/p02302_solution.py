import math

def cross_product(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def point_line_distance(p1, p2, p3):
    return abs(cross_product(p1, p2, p3)) / math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def cut_polygon_area(polygon, line):
    cut_area = 0
    n = len(polygon)
    for i in range(n):
        if cross_product(line[0], line[1], polygon[i]) >= 0:
            cut_area += 0.5*cross_product(polygon[i], polygon[(i+1)%n], line[1])
            if cross_product(line[0], line[1], polygon[(i+1)%n]) < 0:
                cut_area += 0.5*cross_product(polygon[(i+1)%n], line[1], line[0])
    return abs(cut_area)

# Sample Input
polygon = [(1, 1), (4, 1), (4, 3), (1, 3)]
lines = [[(2, 0), (2, 4)], [(2, 4), (2, 0)]]

for line in lines:
    print('{:.8f}'.format(cut_polygon_area(polygon, line)))