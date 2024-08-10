def count_regions(rectangles):
    regions = 1
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i][0] < rectangles[j][2] and rectangles[i][2] > rectangles[j][0] and rectangles[i][1] < rectangles[j][3] and rectangles[i][3] > rectangles[j][1]:
                regions += 1
    return regions

while True:
    n = int(input())
    if n == 0:
        break
    rects = []
    for _ in range(n):
        rects.append(list(map(int, input().split())))
    print(count_regions(rects))