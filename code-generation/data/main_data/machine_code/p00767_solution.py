def integral_rectangles(h, w):
    if w % h == 0:
        new_h = h + 1
        new_w = w
    else:
        new_h = h
        new_w = w + (h - w % h)
    return new_h, new_w

# Read input
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    new_h, new_w = integral_rectangles(h, w)
    print(new_h, new_w)