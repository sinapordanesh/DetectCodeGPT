def construct_polygon(N, angles):
    if sum(angles) != (N-2) * 180:
        return -1
    
    x = 0
    y = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for i in range(N):
        print(x, y)
        if angles[i] == 90:
            x += directions[i % 4][0]
            y += directions[i % 4][1]
        else:
            x += directions[(i-1) % 4][0]
            y += directions[(i-1) % 4][1]
    
    return

# Sample Input 1
N = 8
angles = [90, 90, 270, 90, 90, 90, 270, 90]
construct_polygon(N, angles)

# Sample Input 2
N = 3
angles = [90, 90, 90]
construct_polygon(N, angles)