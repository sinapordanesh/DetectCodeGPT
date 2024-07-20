import math

def smallest_sphere_radius():
    while True:
        n = int(input())
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y, z = map(float, input().split())
            points.append((x, y, z))
        
        max_dist = 0
        for i in range(n):
            for j in range(i+1, n):
                dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2 + (points[i][2] - points[j][2])**2)
                max_dist = max(max_dist, dist)
        
        print("{:.5f}".format(max_dist/2 * math.sqrt(3))) 

smallest_sphere_radius()