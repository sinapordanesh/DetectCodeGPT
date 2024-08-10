def area_of_region(N, M, data):
    segments = []
    for i in range(N):
        segments.append((data[i][0], data[i][2], data[i][1], data[i][2]))
    for j in range(N, N+M):
        segments.append((data[j][0], data[j][1], data[j][0], data[j][2]))
    
    x_max = max(p[0] for p in segments)
    x_min = min(p[0] for p in segments)
    y_max = max(p[1] for p in segments)
    y_min = min(p[1] for p in segments)
    
    if any(x < x_min or x > x_max or y < y_min or y > y_max for x in [0, x_min, x_max] for y in [0, y_min, y_max]):
        return "INF"
    
    area = (x_max - x_min) * (y_max - y_min)
    
    return area

# Sample Input 1
print(area_of_region(5, 6, [(1, 0, 1), (2, 0, 1), (0, 1, 2), (-3, -1, 4), (-2, 3, 6), (1, 1, 0), (0, 2, 1), (2, 2, 0), (-1, 5, -4), (3, 4, -2), (2, 4, 1)]))

# Sample Input 2
print(area_of_region(6, 1, [(-3, -2, -1), (-3, 1, -1), (-2, 2, -1), (1, -2, 4), (1, -1, 4), (1, 1, 4), (3, 4, 1)]))