def min_scatteredness(N, D, coordinates):
    max_x = max(coordinates, key=lambda x: x[0])[0]
    min_x = min(coordinates, key=lambda x: x[0])[0]
    max_y = max(coordinates, key=lambda x: x[1])[1]
    min_y = min(coordinates, key=lambda x: x[1])[1]
    
    min_side_length = max(max_x - min_x, max_y - min_y, D)
    
    print(min_side_length)