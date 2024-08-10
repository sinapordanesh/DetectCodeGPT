def projection(p1_x, p1_y, p2_x, p2_y, q, points):
    def dot_product(p1, p2):
        return p1[0] * p2[0] + p1[1] * p2[1]

    def scale(scalar, p):
        return [scalar * p[0], scalar * p[1]]

    def add(p1, p2):
        return [p1[0] + p2[0], p1[1] + p2[1]]

    def subtract(p1, p2):
        return [p1[0] - p2[0], p1[1] - p2[1]]

    def magnitude(p):
        return (p[0] ** 2 + p[1] ** 2) ** 0.5

    def projection_point(p1, p2, p):
        p1p2 = subtract(p2, p1)
        p1p = subtract(p, p1)
        proj = scale(dot_product(p1p, p1p2) / dot_product(p1p2, p1p2), p1p2)
        projection = add(p1, proj)
        return projection

    for point in points:
        proj = projection_point([p1_x, p1_y], [p2_x, p2_y], point)
        print("{:.10f} {:.10f}".format(proj[0], proj[1]))