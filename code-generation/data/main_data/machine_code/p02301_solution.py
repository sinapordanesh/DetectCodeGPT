import math

def diameter_of_convex_polygon(n, points):
    max_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            max_distance = max(max_distance, distance)
    
    return "{:.10f}".format(max_distance)