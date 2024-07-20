def can_draw_polygon(N, sides):
    sides.sort()
    if sides[-1] < sum(sides[:-1]):
        return "Yes"
    else:
        return "No"

# Sample Input 1
print(can_draw_polygon(4, [3, 8, 5, 1]))

# Sample Input 2
print(can_draw_polygon(4, [3, 8, 4, 1]))

# Sample Input 3
print(can_draw_polygon(10, [1, 8, 10, 5, 8, 12, 34, 100, 11, 3]))