def max_balloon_radius(datasets):
    results = []
    for data in datasets:
        n, w = data[0]
        needles = data[1:]
        max_radius = 100
        for x, y, h in needles:
            max_radius = min(max_radius, min(x, y, 100-x, 100-y, h, w-h))
        results.append('{:.5f}'.format(max_radius))
    return results