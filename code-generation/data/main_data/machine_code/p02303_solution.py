import math

def closest_pair(n, points):
    min_distance = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            distance = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            min_distance = min(min_distance, distance)
    return '{:.6f}'.format(min_distance)

# Sample Input
n = 3
points = [(0.0, 0.0), (2.0, 0.0), (1.0, 1.0)]
print(closest_pair(n, points))