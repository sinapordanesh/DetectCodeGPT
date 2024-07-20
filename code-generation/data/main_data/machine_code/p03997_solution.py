def area_of_trapezoid(a, b, h):
    return (a + b) * h // 2

a, b, h = map(int, input().split())
print(area_of_trapezoid(a, b, h))