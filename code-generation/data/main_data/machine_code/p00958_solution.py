def max_parallel_line_pairs(points):
    pairs = []
    for i in range(0, len(points), 2):
        pairs.append((points[i], points[i + 1]))
    
    max_pairs = 0
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if (pairs[i][0] - pairs[j][0]) * (pairs[i][1] - pairs[j][1]) == -(pairs[i][0] - pairs[j][0]) * (pairs[i][1] - pairs[j][1]):
                max_pairs += 1
    
    return max_pairs

# Read input
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# Output
print(max_parallel_line_pairs(points))