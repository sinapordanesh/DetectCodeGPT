def count_paint_colors(a, b, c):
    colors = {a, b, c}
    return len(colors)

# Test cases
print(count_paint_colors(3, 1, 4))
print(count_paint_colors(3, 3, 33))