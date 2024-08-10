def count_points(N, D, points):
    count = 0
    for point in points:
        distance = (point[0]**2 + point[1]**2)**0.5
        if distance <= D:
            count += 1
    return count