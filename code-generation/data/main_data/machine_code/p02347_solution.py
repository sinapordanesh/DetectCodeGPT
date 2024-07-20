def range_search(n, points, queries):
    result = []
    for query in queries:
        sx, tx, sy, ty = query
        ids = []
        for i in range(n):
            x, y = points[i]
            if sx <= x <= tx and sy <= y <= ty:
                ids.append(i)
        result.extend(sorted(ids))
        result.append("")
    return result

n = 6
points = [(2, 1), (2, 2), (4, 2), (6, 2), (3, 3), (5, 4)]
queries = [(2, 4, 0, 4), (4, 10, 2, 5)]

output = range_search(n, points, queries)
for item in output:
    print(item)