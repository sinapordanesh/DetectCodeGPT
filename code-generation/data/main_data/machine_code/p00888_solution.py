def japanese_alps_route(N, points):
    x1, y1 = points[0]
    xN, yN = points[-1]
    return abs(xN - x1) + 2 * sum(abs(y - y1) for x, y in points[1:-1])

# Sample Input
print(japanese_alps_route(6, [(0, 0), (3, 4), (9, 12), (17, 6), (21, 9), (33, 0)]))
print(japanese_alps_route(5, [(0, 0), (10, 0), (20, 0), (30, 0), (40, 0)]))
print(japanese_alps_route(10, [(0, 0), (1, 2), (3, 0), (6, 3), (9, 0), (11, 2), (13, 0), (15, 2), (16, 2), (18, 0)]))
print(japanese_alps_route(7, [(0, 0), (150, 997), (300, 1), (450, 999), (600, 2), (750, 998), (900, 0)]))