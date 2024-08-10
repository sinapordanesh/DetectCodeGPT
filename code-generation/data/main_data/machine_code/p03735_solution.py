def min_possible_value(N, balls):
    balls.sort(key=lambda x: min(x[0], x[1]))
    red = sorted([max(b[0], b[1]) for b in balls[:N]])
    blue = sorted([max(b[0], b[1]) for b in balls[N:]])
    return (red[N-1] - red[0]) * (blue[N-1] - blue[0])