def ink_consumption(n, w, values):
    total_area = sum(values)
    max_value = max(values)
    max_area = max_value * w / n
    dark_levels = [1 - i/(n-1) for i in range(n)]
    ink = sum([(area / max_area) * dark for area, dark in zip(values, dark_levels)])
    ink += 0.01
    return ink

print(ink_consumption(3, 50, [100, 0, 100]))
print(ink_consumption(3, 50, [100, 100, 50]))
print(ink_consumption(10, 10, [1, 2, 3, 4, 5, 16, 17, 18, 29, 30]))