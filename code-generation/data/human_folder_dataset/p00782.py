import sys

def is_contained(a, area):
    rx1, ry1, rx2, ry2 = a
    for r in area:
        x1, y1, x2, y2 = r
        if x1 <= rx1 <= x2 and x1 <= rx2 <= x2 and \
           y1 <= ry1 <= y2 and y1 <= ry2 <= y2:
            return True
    return False

def add_area(a, area):
    if is_contained(a, area):
        return area
    xs, ys, xe, ye = a
    if xs >= xe or ys >= ye:
        return area
    ret = area
    if area == []:
        return [a]
    rr = []
    for r in area:
        rxs, rys, rxe, rye = r
        if xs < rxs < xe and ys < rys < ye and xe <= rxe and ye <= rye:
            rr = [[xs, ys, xe, rys], [xs, rys, rxs, ye]]
        elif xs < rxs < xe and ys < rye < ye and rys <= ys and xe <= rxe:
            rr = [[xs, ys, rxs, rye], [xs, rye, xe, ye]]
        elif xs < rxe < xe and ys < rys < ye and rxs <= xs and ye <= rye:
            rr = [[xs, ys, rxe, rys], [rxe, ys, xe, ye]]
        elif xs < rxe < xe and ys < rye < ye and rxs <= xs and rys <= ys:
            rr = [[xs, rye, rxe, ye], [rxe, ys, xe, ye]]
        elif xs < rxs and ys <= rys < ye and rxe < xe and ye <= rye:
            rr = [[xs, ys, xe, rys], [xs, rys, rxs, ye], [rxe, rys, xe, ye]]
        elif xs < rxs and ys < rye <= ye and rxe < xe and rys <= ys:
            rr = [[xs, rye, xe, ye], [xs, ys, rxs, rye], [rxe, ys, xe, rye]]
        elif xs <= rxs < xe and ys < rys and rye < ye and xe <= rxe:
            rr = [[xs, ys, rxs, ye], [rxs, ys, xe, rys], [rxs, rye, xe, ye]]
        elif xs < rxe <= xe and ys < rys and rye < ye and rxs <= xs:
            rr = [[rxe, ys, xe, ye], [xs, ys, rxe, rys], [xs, rye, rxe, ye]]
        elif rxs <= xs and xe <= rxe and ys < rys < ye and ye <= rye:
            rr = [[xs, ys, xe, rys]]
        elif rys <= ys and ye <= rye and xs < rxs < xe and xe <= rxe:
            rr = [[xs, ys, rxs, ye]]
        elif rxs <= xs and xe <= rxe and ys < rye < ye and rys <= ys:
            rr = [[xs, rye, xe, ye]]
        elif rys <= ys and ye <= rye and xs < rxe < xe and rxs <= xs:
            rr = [[rxe, ys, xe, ye]]
        elif xs < rxs < xe and xs < rxe < xe and ys < rys < ye and ys < rye < ye:
            rr = [[xs, ys, rxs, rye], [xs, rye, rxe, ye], [rxe, rys, xe, ye], [rxs, ys, xe, rys]]
        elif rxs <= xs and xe <= rxe and ys < rys and rye < ye:
            rr = [[xs, ys, xe, rys], [xs, rye, xe, ye]]
        elif rys <= ys and ye <= rye and xs < rxs and rxe < xe:
            rr = [[xs, ys, rxs, ye], [rxe, ys, xe, ye]]
        if rr != []:
            for q in rr:
                ret = add_area(q, ret)
            break
    if rr == []:
        ret.append(a)
    return ret

def calc_area(area):
    s = 0.0
    for r in area:
        s += (r[2]- r[0]) * (r[3] - r[1])
    return s

n = 0
c = 0
area = []
for line in sys.stdin:
    if n == 0:
        n = int(line)
        c += 1
        area = []
        if n == 0:
            break
    else:
        ant = list(map(float, line.strip().split()))
        r = [ant[0] - ant[2], ant[1] - ant[2], ant[0] + ant[2], ant[1] + ant[2]]
        area = add_area(r, area)
        n -= 1
        if n == 0:
            print("%d %.2f" % (c, calc_area(area)))
