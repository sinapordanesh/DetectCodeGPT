import math

def find_triangle_area(n, k):
    def count_triangles_with_area(area):
        count = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for l in range(j+1, n+1):
                    a = math.sqrt(sum([(x-y)**2 for x, y in zip(points[i], points[j])]))
                    b = math.sqrt(sum([(x-y)**2 for x, y in zip(points[j], points[l])]))
                    c = math.sqrt(sum([(x-y)**2 for x, y in zip(points[l], points[i])]))
                    s = 0.5 * (a + b + c)
                    triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                    if math.isclose(triangle_area, area):
                        count += 1
        return count

    points = [(0, 0)]
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    possible_areas = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for l in range(j+1, n+1):
                a = math.sqrt(sum([(x-y)**2 for x, y in zip(points[i], points[j])]))
                b = math.sqrt(sum([(x-y)**2 for x, y in zip(points[j], points[l])]))
                c = math.sqrt(sum([(x-y)**2 for x, y in zip(points[l], points[i])]))
                s = 0.5 * (a + b + c)
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                possible_areas.append(area)

    possible_areas = list(set(possible_areas))
    possible_areas.sort()

    low = 0
    high = possible_areas[-1]
    while low < high:
        mid = (low + high) / 2
        if count_triangles_with_area(mid) < k:
            low = mid + 1e-11
        else:
            high = mid

    return "{:.12f}".format(low)

# Sample Input
n, k = map(int, input().split())
print(find_triangle_area(n, k))