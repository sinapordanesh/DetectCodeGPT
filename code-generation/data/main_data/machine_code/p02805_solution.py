import math

def min_circle_radius(n, points):
    def dist(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    radius = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            center_x = (points[i][0] + points[j][0]) / 2
            center_y = (points[i][1] + points[j][1]) / 2
            max_dist = max(dist(points[i], points[j]) / 2, max(dist(points[i], [center_x, center_y]), dist(points[j], [center_x, center_y])))
            radius = min(radius, max_dist)

    return radius

# Input
n = 2
points = [(0, 0), (1, 0)]

# Output
print("{:.15f}".format(min_circle_radius(n, points)))

# Input
n = 3
points = [(0, 0), (0, 1), (1, 0)]

# Output
print("{:.15f}".format(min_circle_radius(n, points)))

# Input
n = 10
points = [(10, 9), (5, 9), (2, 0), (0, 0), (2, 7), (3, 3), (2, 5), (10, 0), (3, 7), (1, 9)]

# Output
print("{:.15f}".format(min_circle_radius(n, points)))