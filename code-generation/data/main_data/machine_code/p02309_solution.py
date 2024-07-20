def cross_points_of_circles():
    c1x, c1y, c1r = map(int, input().split())
    c2x, c2y, c2r = map(int, input().split())

    d = ((c1x - c2x) ** 2 + (c1y - c2y) ** 2) ** 0.5
    a = (c1r**2 - c2r**2 + d**2) / (2 * d)
    h = (c1r**2 - a**2) ** 0.5

    x1 = c1x + a * (c2x - c1x) / d
    y1 = c1y + a * (c2y - c1y) / d
    x2 = x1 + h * (c2y - c1y) / d
    y2 = y1 - h * (c2x - c1x) / d

    print("{:.8f} {:.8f} {:.8f} {:.8f}".format(x2, y2, x1, y1))

cross_points_of_circles()