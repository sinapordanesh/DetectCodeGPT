from math import pi, cos, sin
def solve():
    def rotate(x, y, theta):
        cv = cos(theta); sv = sin(theta)
        return x*cv - y*sv, x*sv + y*cv
    N, D = map(int, input().split())
    if N == D == 0:
        return False
    x0 = -D; x1 = D
    y0 = y1 = 0
    for i in range(N):
        dl, dr, t = map(int, input().split())
        if dl ^ dr >= 0:
            if dl == dr:
                dx = x1 - x0; dy = y1 - y0
                a = pi * dl * t / 180
                dx1 = -dy * a / (2*D); dy1 = dx * a / (2*D)
                x0 += dx1; x1 += dx1
                y0 += dy1; y1 += dy1
            elif dl > dr:
                x2 = (dl * x1 - dr * x0) / (dl - dr)
                y2 = (dl * y1 - dr * y0) / (dl - dr)
                theta = pi * (dl - dr) * t / (360 * D)
                dx, dy = rotate(x0 - x2, y0 - y2, -theta)
                x0 = x2 + dx; y0 = y2 + dy
                dx, dy = rotate(x1 - x2, y1 - y2, -theta)
                x1 = x2 + dx; y1 = y2 + dy
            else:
                x2 = (dr * x0 - dl * x1) / (dr - dl)
                y2 = (dr * y0 - dl * y1) / (dr - dl)
                theta = pi * (dr - dl) * t / (360 * D)
                dx, dy = rotate(x0 - x2, y0 - y2, theta)
                x0 = x2 + dx; y0 = y2 + dy
                dx, dy = rotate(x1 - x2, y1 - y2, theta)
                x1 = x2 + dx; y1 = y2 + dy
        else:
            if dl > dr:
                x2 = (- dr * x0 + dl * x1) / (dl - dr)
                y2 = (- dr * y0 + dl * y1) / (dl - dr)
                theta = pi * (dl - dr) * t / (360 * D)
                dx, dy = rotate(x0 - x2, y0 - y2, -theta)
                x0 = x2 + dx; y0 = y2 + dy
                dx, dy = rotate(x1 - x2, y1 - y2, -theta)
                x1 = x2 + dx; y1 = y2 + dy
            else:
                x2 = (dr * x0 - dl * x1) / (- dl + dr)
                y2 = (dr * y0 - dl * y1) / (- dl + dr)
                theta = pi * (- dl + dr) * t / (360 * D)
                dx, dy = rotate(x0 - x2, y0 - y2, theta)
                x0 = x2 + dx; y0 = y2 + dy
                dx, dy = rotate(x1 - x2, y1 - y2, theta)
                x1 = x2 + dx; y1 = y2 + dy
    print("%.16f" % ((x0 + x1) / 2))
    print("%.16f" % ((y0 + y1) / 2))
    return True
while solve():
    ...
