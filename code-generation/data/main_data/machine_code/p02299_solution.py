def PolygonPointContainment(g, queries):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def on_segment(p, q, r):
        if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and 
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
            return True
        return False

    def is_inside_polygon(polygon, query):
        n = len(polygon)
        if n < 3:
            return False
        extreme = (float('inf'), query[1])
        count = 0
        i = 0
        while True:
            next_ = (i + 1) % n
            if on_segment(polygon[i], polygon[next_], query):
                return 1
            o = orientation(polygon[i], query, polygon[next_])
            if (o == 0):
                return 1
            if (polygon[i][1] < query[1] and polygon[next_][1] >= query[1]) or (polygon[next_][1] < query[1] and polygon[i][1] >= query[1]):
                if (polygon[i][0] + (query[1] - polygon[i][1]) / (polygon[next_][1] - polygon[i][1]) * (polygon[next_][0] - polygon[i][0]) < query[0]):
                    count += 1
            i = next_
            if i == 0:
                break
        return count % 2 == 1

    polygon = [tuple(map(int, point.split())) for point in g.split('\n')[1:-1]]
    results = []
    for query in queries:
        query_point = tuple(map(int, query.split()))
        if is_inside_polygon(polygon, query_point):
            results.append(2)
        elif query_point in polygon:
            results.append(1)
        else:
            results.append(0)
    return results

# Sample Input
g = "4\n0 0\n3 1\n2 3\n0 3\n"
queries = ["2 1", "0 2", "3 2"]
print(PolygonPointContainment(g, queries))