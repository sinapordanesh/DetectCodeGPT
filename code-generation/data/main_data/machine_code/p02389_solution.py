def rectangle_properties():
    a, b = map(int, input().split())
    area = a * b
    perimeter = 2 * (a + b)
    print(area, perimeter)

rectangle_properties()