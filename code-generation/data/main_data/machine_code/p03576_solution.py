def min_rectangle_area(N, K, points):
    min_area = float('inf')
    for i in range(N):
        for j in range(i+K-1, N):
            x_values = [points[k][0] for k in range(i, j+1)]
            y_values = [points[k][1] for k in range(i, j+1)]
            min_x = min(x_values)
            max_x = max(x_values)
            min_y = min(y_values)
            max_y = max(y_values)
            area = (max_x - min_x) * (max_y - min_y)
            min_area = min(min_area, area)
    return min_area

# Input
N, K = map(int, input().split())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# Output
print(min_rectangle_area(N, K, points))