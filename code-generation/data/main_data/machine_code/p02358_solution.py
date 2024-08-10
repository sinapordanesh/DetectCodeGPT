def union_of_rectangles(N, rectangles):
    area = 0
    for i in range(N):
        area += (rectangles[i][2] - rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1])
    
    for i in range(N):
        for j in range(i+1, N):
            x_overlap = max(0, min(rectangles[i][2], rectangles[j][2]) - max(rectangles[i][0], rectangles[j][0]))
            y_overlap = max(0, min(rectangles[i][3], rectangles[j][3]) - max(rectangles[i][1], rectangles[j][1]))
            area -= x_overlap * y_overlap
    
    return area

N = int(input())
rectangles = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append((x1, y1, x2, y2))

print(union_of_rectangles(N, rectangles))