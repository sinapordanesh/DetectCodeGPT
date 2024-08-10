def clock_hands_overlap(H, h, m, s):
    while True:
        s += 1
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
        if h == H:
            h = 0
        if H == 12:
            a1 = (30 * h + 0.5 * m + 0.0083333 * s) % 360
            a2 = (6 * m + 0.1 * s) % 360
            if round(a1 - a2, 7) == 0:
                return h, m, s, 1
        else:
            a1 = (360 / H * h + 30 / H * m + 0.5 / H * s) % 360
            a2 = (6 * m + 0.1 * s) % 360
            if round(a1 - a2, 7) == 0:
                return h, m, s, 1

        if s == 0 and m == 0:
            h = (h + 1) % H

H, h, m, s = map(int, input().split())
while not (H == h == m == s == 0):
    result = clock_hands_overlap(H, h, m, s)
    print(*result)
    H, h, m, s = map(int, input().split())