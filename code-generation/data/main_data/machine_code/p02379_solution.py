def distance(x1, y1, x2, y2):
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print("{:.8f}".format(dist))

# Sample Input
distance(0, 0, 1, 1)