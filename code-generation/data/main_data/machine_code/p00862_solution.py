import math

def distance_from_sea(n, points):
    max_distance = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        max_distance = max(max_distance, distance)
    return max_distance
