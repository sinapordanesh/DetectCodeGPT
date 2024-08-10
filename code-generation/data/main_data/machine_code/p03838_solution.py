def min_press(x, y):
    diff = abs(y - x)
    if (y - x) * (y - x) < 0:
        return diff + 1
    else:
        return diff

x, y = map(int, input().split())
print(min_press(x, y))