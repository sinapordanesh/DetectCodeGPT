import math

def chain_confined_path(n, circles):
    total_distance = 0
    for i in range(n-1):
        x1, y1, r1 = circles[i]
        x2, y2, r2 = circles[i+1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) - (r1 + r2)
        total_distance += max(distance, 0)
    return total_distance

while True:
    n = int(input())
    if n == 0:
        break
    circles = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    result = chain_confined_path(n, circles)
    print(result)