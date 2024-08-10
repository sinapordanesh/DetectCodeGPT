def circles_intersection(N, datasets):
    for data in datasets:
        xa, ya, ra, xb, yb, rb = data
        distance = ((xb - xa)**2 + (yb - ya)**2)**0.5
        if distance + rb < ra:
            print("2")
        elif distance + ra < rb:
            print("-2")
        elif distance == ra + rb:
            print("1")
        else:
            print("0")

N = 2
datasets = [(0.0, 0.0, 5.0, 0.0, 0.0, 4.0), (0.0, 0.0, 2.0, 4.1, 0.0, 2.0)]
circles_intersection(N, datasets)