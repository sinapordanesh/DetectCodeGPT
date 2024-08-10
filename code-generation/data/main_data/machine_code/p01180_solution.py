import math

def closest_circle_distance(N, circles):
    min_distance = float('inf')
    for i in range(N):
        for j in range(i+1, N):
            distance = math.sqrt((circles[i][1] - circles[j][1])**2 + (circles[i][2] - circles[j][2])**2) - circles[i][0] - circles[j][0]
            min_distance = min(min_distance, distance)
    return min_distance

# Sample Input
N = 4
circles = [(1.0, 0.0, 0.0), (1.5, 0.0, 3.0), (2.0, 4.0, 0.0), (1.0, 3.0, 4.0)]

print(closest_circle_distance(N, circles))