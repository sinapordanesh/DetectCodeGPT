import math

def chocolate_cutting():
    n = int(input())
    vertices = []
    for _ in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))

    area = 0
    for i in range(n):
        area += (vertices[i][0] * vertices[(i + 1) % n][1]) - (vertices[i][1] * vertices[(i + 1) % n][0])
    area /= 2

    min_length = float('inf')
    max_length = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]

        a = y2 - y1
        b = x1 - x2
        c = (x1 * y2) - (x2 * y1)

        temp = (a * x1) + (b * y1) + c
        length = abs(temp) / math.sqrt((a ** 2) + (b ** 2))

        min_length = min(min_length, length)
        max_length = max(max_length, length)

    print(min_length)
    print(max_length)

chocolate_cutting()