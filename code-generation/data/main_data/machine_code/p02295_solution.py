def cross_point(q, queries):
    for i in range(q):
        p0, p1, p2, p3 = queries[i]
        x = (p0[0] * p1[1] - p0[1] * p1[0]) * (p2[0] - p3[0]) - (p0[0] - p1[0]) * (p2[0] * p3[1] - p2[1] * p3[0])
        y = (p0[0] * p1[1] - p0[1] * p1[0]) * (p2[1] - p3[1]) - (p0[1] - p1[1]) * (p2[0] * p3[1] - p2[1] * p3[0])
        det = (p0[0] - p1[0]) * (p2[1] - p3[1]) - (p0[1] - p1[1]) * (p2[0] - p3[0])
        x /= det
        y /= det
        print(f"{x:.10f} {y:.10f}")

# Sample Input
q = 3
queries = [
    [(0, 0), (2, 0), (1, 1), (1, -1)],
    [(0, 0), (1, 1), (0, 1), (1, 0)],
    [(0, 0), (1, 1), (1, 0), (0, 1)]
]

cross_point(q, queries)