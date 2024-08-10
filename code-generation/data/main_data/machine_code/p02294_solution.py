def intersection(q, queries):
    for i in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = queries[i]
        if (x0-x1)*(y2-y3) - (y0-y1)*(x2-x3) != 0:
            print("1")
        else:
            print("0")