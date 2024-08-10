def calculate_intersection_volume(prism_data):
    m, n = prism_data[0]
    points_C1 = prism_data[1:m+1]
    points_C2 = prism_data[m+1:]
    
    volume = 0.0
    for i in range(m):
        x1, y1 = points_C1[i]
        x2, y2 = points_C1[(i + 1) % m]
        
        for j in range(n):
            x3, z3 = points_C2[j]
            x4, z4 = points_C2[(j + 1) % n]
            
            volume += ((x2 - x1) * (z4 - z3) - (z2 - z1) * (x4 - x3)) * min(y1, y2, z3, z4)
    
    return abs(volume) / 2

# Read input from stdin
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    prism_data = []
    prism_data.append((m, n))
    for _ in range(m + n):
        prism_data.append(tuple(map(int, input().split())))
    
    result = calculate_intersection_volume(prism_data)
    print(result)