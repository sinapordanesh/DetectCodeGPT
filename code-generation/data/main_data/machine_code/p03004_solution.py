import sys

def find_min_area(N, points):
    x_values = []
    y_values = []
    
    for point in points:
        x, y, d = point
        x_values.append(x) if d in ['R', 'L'] else None
        y_values.append(y) if d in ['U', 'D'] else None
    
    x_diff = max(x_values) - min(x_values)
    y_diff = max(y_values) - min(y_values)
    
    return x_diff * y_diff

# Input
input_lines = sys.stdin.readlines()
N = int(input_lines[0])
points = [list(map(int, line.strip().split())) for line in input_lines[1:]]

# Output
print(find_min_area(N, points))