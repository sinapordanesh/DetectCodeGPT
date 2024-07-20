def koch_curve(n):
    def koch(p1, p2, depth):
        if depth == 0:
            print("{:.8f} {:.8f}".format(p1[0], p1[1]))
        else:
            s = ((2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3)
            t = ((p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3)
            u = ((t[0] - s[0]) * 0.5 - (t[1] - s[1]) * (3**0.5 * 0.5) + s[0],
                 (t[0] - s[0]) * (3**0.5 * 0.5) + (t[1] - s[1]) * 0.5 + s[1])
            koch(p1, s, depth - 1)
            koch(s, u, depth - 1)
            koch(u, t, depth - 1)
            koch(t, p2, depth - 1)

    koch((0, 0), (100, 0), n)

n = int(input())
koch_curve(n)