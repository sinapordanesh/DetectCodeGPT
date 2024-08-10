def calculate_weights(a, b, d):
    x = 0
    y = 0

    while d > 0:
        if d >= a:
            x += 1
            d -= a
        elif d >= b:
            y += 1
            d -= b

    return x, y