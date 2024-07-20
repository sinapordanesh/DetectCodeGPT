def altitude_approximation(w, d, n, measurements):
    altitudes = [[float('inf')] * w for _ in range(d)]

    for i in range(n):
        x, y, z = measurements[i]
        altitudes[y-1][x-1] = z

    while True:
        modified = False
        for y in range(d):
            for x in range(w):
                z = altitudes[y][x]
                for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < d and 0 <= nx < w:
                        nz = altitudes[ny][nx]
                        if abs(z - nz) > 1:
                            altitudes[ny][nx] = min(altitudes[ny][nx], z + 1)
                            modified = True

        if not modified:
            break

    total_altitude = sum(sum(row) for row in altitudes)
    return total_altitude

# Sample Input
print(altitude_approximation(5, 4, 2, [(1, 1, 10), (5, 4, 3)]))
print(altitude_approximation(5, 4, 3, [(2, 2, 0), (4, 3, 0), (5, 1, 2)]))
print(altitude_approximation(3, 3, 2, [(1, 1, 8), (3, 3, 3)]))
print(altitude_approximation(2, 2, 1, [(1, 1, -100)]))