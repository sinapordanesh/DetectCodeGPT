def voronoi_island(N, M, vertices, castles):
    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def area(v1, v2, v3):
        return abs((v1[0] * (v2[1] - v3[1]) + v2[0] * (v3[1] - v1[1]) + v3[0] * (v1[1] - v2[1])) / 2)

    areas = []
    for castle in castles:
        total_area = 0
        for i in range(N):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % N]
            x3, y3 = castle
            total_area += area((x1, y1), (x2, y2), (x3, y3))

        areas.append(total_area)

    return areas

# Sample Input
N = 3
M = 3
vertices = [(0, 0), (8, 0), (0, 8)]
castles = [(2, 2), (4, 2), (2, 4)]

output = voronoi_island(N, M, vertices, castles)
for area in output:
    print(area)