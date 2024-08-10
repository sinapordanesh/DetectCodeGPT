digits = "-0123456789"
def cross_point(P, Q):
    x0, y0, x1, y1 = P
    x2, y2, x3, y3 = Q
    dx0 = x1 - x0; dy0 = y1 - y0
    dx1 = x3 - x2; dy1 = y3 - y2

    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if s < 0:
        s = -s
        sm = -sm
    if s == 0:
        x = x0
        y = y0
    else:
        x = x0 + s*dx0/sm
        y = y0 + s*dy0/sm
    return x, y
def reflection(line, point):
    x0, y0, x1, y1 = line
    p, q = point
    x1 -= x0; y1 -= y0
    p -= x0; q -= y0
    cv = p*x1 + q*y1
    sv = p*y1 - q*x1
    cv2 = cv**2 - sv**2
    sv2 = 2*cv*sv
    dd = (p**2 + q**2)*(x1**2 + y1**2)
    if dd == 0:
        return x0 + p, y0 + q
    return x0 + (cv2 * p - sv2 * q) / dd, y0 + (sv2 * p + cv2 * q) / dd

def parse(S):
    S = S + "$"
    cur = 0
    def expr():
        nonlocal cur
        res = None
        while S[cur] == '(':
            cur += 1 # '('
            if S[cur] in digits:
                x = number()
                cur += 1 # ','
                y = number()
                r = (0, x, y)
            else:
                r = expr()
            cur += 1 # ')'
            if res is None:
                res = r
            else:
                if res[0] == r[0] == 0:
                    # (point)@(point)
                    res = (1, res[1], res[2], r[1], r[2])
                elif res[0] == r[0] == 1:
                    # (line)@(line)
                    x, y = cross_point(res[1:], r[1:])
                    res = (0, x, y)
                else:
                    # (line)@(point) or (point)@(line)
                    point, line = (res, r) if r[0] else (r, res)
                    x, y = reflection(line[1:], point[1:])
                    res = (0, x, y)
            if S[cur] != '@':
                break
            cur += 1 # '@'
        return res

    def number():
        nonlocal cur
        v = 0; mns = 0
        if S[cur] == '-':
            mns = 1
            cur += 1 # '-'
        while S[cur] in digits:
            v = 10*v + int(S[cur])
            cur += 1
        return -v if mns else v

    return expr()

def solve():
    s = input()
    if s == '#':
        return False
    res = parse(s)
    print("%.16f %.16f" % res[1:])
    return True
while solve():
    ...
