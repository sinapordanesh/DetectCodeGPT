def circle_in_rectangle(W, H, x, y, r):
    if (x - r >= 0) and (y - r >= 0) and (x + r <= W) and (y + r <= H):
        return "Yes"
    else:
        return "No"

# Sample Input
print(circle_in_rectangle(5, 4, 2, 2, 1))
print(circle_in_rectangle(5, 4, 2, 4, 1))