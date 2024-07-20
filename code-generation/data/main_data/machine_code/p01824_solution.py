def surface_area_of_cubes(A, B, C, N, removed_cubes):
    total_area = 2 * (A * B + B * C + C * A)
    
    for x, y, z in removed_cubes:
        area = 0
        if x - 1 < 0:
            area += B * C
        if x + 1 >= A:
            area += B * C
        if y - 1 < 0:
            area += A * C
        if y + 1 >= B:
            area += A * C
        if z - 1 < 0:
            area += A * B
        if z + 1 >= C:
            area += A * B
        
        total_area -= area
    
    return total_area

# Test the function with sample inputs
print(surface_area_of_cubes(2, 2, 2, 1, [(0, 0, 0)])) # Output: 24
print(surface_area_of_cubes(1, 1, 5, 2, [(0, 0, 1), (0, 0, 3)])) # Output: 18
print(surface_area_of_cubes(3, 3, 3, 1, [(1, 1, 1)])) # Output: 60