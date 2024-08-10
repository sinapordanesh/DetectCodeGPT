import math

def get_circle_center_and_radius1(x1, y1, x2, y2, x3, y3):
    """
    3点を通る円の中心と半径を取得
    """
    d = 2 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    if d == 0:
        return (0, 0), 0
    x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2) * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
    y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2) * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
    r = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    return (x, y), r


def get_circle_center_and_radius2(x1, y1, x2, y2):
    x = (x2 + x1) / 2
    y = (y2 + y1) / 2
    r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 / 2
    return (x, y), r


n = int(input())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)


ans = 10 ** 9
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x1 = xs[i]
            y1 = ys[i]
            x2 = xs[j]
            y2 = ys[j]
            x3 = xs[k]
            y3 = ys[k]
            (x, y), r = get_circle_center_and_radius1(x1, y1, x2, y2, x3, y3)
            if r == 0:
                continue
            ok = True
            for l in range(n):
                if l in [i, j, k]:
                    continue
                if (x - xs[l]) ** 2 + (y - ys[l]) ** 2 > r ** 2:
                    ok = False
                    break
            if ok:
                ans = min(ans, r)

for i in range(n - 1):
    for j in range(i + 1, n):
        x1 = xs[i]
        y1 = ys[i]
        x2 = xs[j]
        y2 = ys[j]
        (x, y), r = get_circle_center_and_radius2(x1, y1, x2, y2)
        ok = True
        for l in range(n):
            if l in [i, j]:
                continue
            if (x - xs[l]) ** 2 + (y - ys[l]) ** 2 > r ** 2:
                ok = False
                break
        if ok:
            ans = min(ans, r)

print(ans)
