def max_manhattan_distance(N, points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    
    max_x = max(x_values)
    min_x = min(x_values)
    max_y = max(y_values)
    min_y = min(y_values)
    
    return max(max_x - min_x, max_y - min_y)