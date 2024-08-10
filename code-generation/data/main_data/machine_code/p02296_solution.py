def distance_between_segments(q, queries):
    def distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    
    for query in queries:
        p0 = (query[0], query[1])
        p1 = (query[2], query[3])
        p2 = (query[4], query[5])
        p3 = (query[6], query[7])
        
        if (p1[0] - p0[0]) * (p3[1] - p2[1]) == (p1[1] - p0[1]) * (p3[0] - p2[0]):
            print("0.0000000000")
        else:
            d1 = distance(p0, p2)
            d2 = distance(p0, p3)
            d3 = distance(p1, p2)
            d4 = distance(p1, p3)
            print("{:.10f}".format(min(d1, d2, d3, d4)))

# Sample input
distance_between_segments(3, [(0, 0, 1, 0, 0, 1, 1, 1), (0, 0, 1, 0, 2, 1, 1, 2), (-1, 0, 1, 0, 0, 1, 0, -1)])