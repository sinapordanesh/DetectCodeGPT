def area_of_polygons():
    while True:
        num_vertices = int(input())
        if num_vertices == 0:
            break
        vertices = []
        for _ in range(num_vertices):
            x, y = map(int, input().split())
            vertices.append((x, y))
        total_area = 0
        for i in range(num_vertices):
            total_area += (vertices[i][0] * vertices[(i + 1) % num_vertices][1]) - (vertices[i][1] * vertices[(i + 1) % num_vertices][0])
        print(abs(total_area) // 2)

area_of_polygons()