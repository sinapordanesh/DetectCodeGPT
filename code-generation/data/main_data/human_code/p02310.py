from math import pi, cos, sin, atan2
EPS = 10**(-9)

def eq(value1, value2):
    return abs(value1-value2) <= EPS

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.arg = atan2(y, x) # -PI ~ PI
    
    def __str__(self):
        return "{0:.8f} {1:.8f}".format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scal):
        return Point(self.x*scal, self.y*scal)
    
    def __truediv__(self, scal):
        return Point(self.x/scal, self.y/scal)
    
    def __eq__(self, other):
        return eq(self.x, other.x) and eq(self.y, other.y)

    # 原点からの距離
    def __abs__(self):
        return (self.x**2+self.y**2)**0.5
    
# 原点を中心にrad角だけ回転した点
def Rotation(vec: Point, rad):
    return Point(vec.x*cos(rad)-vec.y*sin(rad), vec.x*sin(rad)+vec.y*cos(rad))


class Circle():
    def __init__(self, p, r):
        self.p = p
        self.r = r


class Line():
    # 点a, bを通る
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.arg = (a-b).arg % pi
    
    def __str__(self):
        return "[({0}, {1}) - ({2}, {3})]".format(self.a.x, self.a.y, self.b.x, self.b.y)

    # pointを通って平行
    def par(self, point):
        return Line(point, point+(self.a-self.b))

    # pointを通って垂直
    def tan(self, point):
        return Line(point, point + Rotation(self.a-self.b, pi/2))


class Segment(Line):
    def __init__(self, a, b):
        super().__init__(a, b)


# 符号付き面積
def cross(vec1: Point, vec2: Point):
    return vec1.x*vec2.y - vec1.y*vec2.x

# 内積
def dot(vec1: Point, vec2: Point):
    return vec1.x*vec2.x + vec1.y*vec2.y

# 点a->b->cの回転方向
def ccw(a, b, c):
    if cross(b-a, c-a) > EPS: return +1 # COUNTER_CLOCKWISE
    if cross(b-a, c-a) < -EPS: return -1 # CLOCKWISE
    if dot(c-a, b-a) < -EPS: return +2 # c -> a -> b
    if abs(b-a) < abs(c-a): return -2 # a -> b -> c
    return 0 # a -> c -> b


# pのlへの射影
def projection(l, p):
    t = dot(l.b-l.a, p-l.a) / abs(l.a-l.b)**2
    return l.a + (l.b-l.a)*t

# pのlによる反射
def reflection(l, p):
    return p + (projection(l, p) - p)*2

def isPararell(l1, l2):
    return eq(cross(l1.a-l1.b, l2.a-l2.b), 0)

def isVertical(l1, l2):
    return eq(dot(l1.a-l1.b, l2.a-l2.b), 0)


def isIntersect_lp(l, p):
    return abs(ccw(l.a, l.b, p)) != 1

def isIntersect_ll(l1, l2):
    return not isPararell(l1, l2) or isIntersect_lp(l1, l2.a)

def isIntersect_sp(s, p):
    return ccw(s.a, s.b, p) == 0

def isIntersect_ss(s1, s2):
    return ccw(s1.a, s1.b, s2.a)*ccw(s1.a, s1.b, s2.b) <= 0 and ccw(s2.a, s2.b, s1.a)*ccw(s2.a, s2.b, s1.b) <= 0

def isIntersect_ls(l, s):
    return cross(l.b - l.a, s.a - l.a) * cross(l.b - l.a, s.b - l.a) < EPS

def isIntersect_cp(c, p):
    return abs(abs(c.p - p) - c.r) < EPS

def isIntersect_cl(c, l):
    return distance_lp(l, c.p) <= c.r + EPS

def isIntersect_cs(c, s):
    pass

def intersect_cc(c1, c2):
    if c1.r < c2.r:
        c1, c2 = c2, c1
    d = abs(c1.p - c2.p)
    if eq(c1.r + c2.r, d): return 3 # 内接
    if eq(c1.r - c2.r, d): return 1 # 外接
    if c1.r + c2.r < d: return 4 # 含まれてる
    if c1.r - c2.r < d: return 2 # 2交点持つ
    return 0 # 離れてる


def distance_pp(p1, p2):
    return abs(p1-p2)

def distance_lp(l, p):
    return abs(projection(l,p)-p)

def distance_ll(l1, l2):
    return 0 if isIntersect_ll(l1, l2) else distance_lp(l1, l2.a)

def distance_sp(s, p):
    r = projection(s, p)
    if isIntersect_sp(s, r): return abs(r-p)
    return min(abs(s.a-p), abs(s.b-p))

def distance_ss(s1, s2):
    if isIntersect_ss(s1, s2): return 0
    return min([distance_sp(s1, s2.a), distance_sp(s1, s2.b), distance_sp(s2, s1.a), distance_sp(s2, s1.b)])

def distance_ls(l, s):
    if isIntersect_ls(l, s): return 0
    return min(distance_lp(l, s.a), distance_lp(l, s.b))


def crosspoint_ll(l1, l2):
    A = cross(l1.b - l1.a, l2.b - l2.a)
    B = cross(l1.b - l1.a, l1.b - l2.a)
    if eq(abs(A), 0) and eq(abs(B), 0): return l2.a
    return l2.a + (l2.b - l2.a) * B / A

def crosspoint_ss(s1, s2):
    return crosspoint_ll(s1, s2)

def crosspoint_lc(l, c):
    p = projection(l, c.p)
    if eq(distance_lp(l, c.p), c.r): return [p]
    e = (l.b - l.a) / abs(l.b-l.a)
    dis = (c.r**2-abs(p-c.p)**2)**0.5
    return [p + e*dis, p - e*dis]

def crosspoint_sc(s, c):
    pass

def crosspoint_cc(c1, c2):
    d = abs(c1.p-c2.p)
    if not abs(c1.r-c2.r) <= d <= c1.r+c2.r:
        return []
    mid_p = (c2.p * (c1.r**2-c2.r**2+d**2) + c1.p * (c2.r**2-c1.r**2+d**2)) / (2*d**2)
    tanvec = Rotation(c1.p-c2.p, pi/2)
    return crosspoint_lc(Line(mid_p, mid_p+tanvec), c1)


# pからのcの接点
def tangent_cp(c, p):
    return crosspoint_cc(c, Circle(p, (abs(p-c.p)**2 - c.r**2)**0.5))





import sys
input = sys.stdin.readline

def verify_1A():
    p1x, p1y, p2x, p2y = map(int, input().split())
    l = Line(Point(p1x, p1y), Point(p2x, p2y))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for px, py in Query:
        p = Point(px, py)
        print(projection(l, p))

def verify_1B():
    p1x, p1y, p2x, p2y = map(int, input().split())
    l = Line(Point(p1x, p1y), Point(p2x, p2y))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for px, py in Query:
        p = Point(px, py)
        print(reflection(l, p))

def verify_1C():
    p1x, p1y, p2x, p2y = map(int, input().split())
    p1 = Point(p1x, p1y); p2 = Point(p2x, p2y)
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for px, py in Query:
        p = Point(px, py)
        result = ccw(p1, p2, p)
        if result == 1:
            print("COUNTER_CLOCKWISE")
        elif result == -1:
            print("CLOCKWISE")
        elif result == 2:
            print("ONLINE_BACK")
        elif result == -2:
            print("ONLINE_FRONT")
        else:
            print("ON_SEGMENT")

def verify_2A():
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y in Query:
        l1 = Line(Point(p0x, p0y), Point(p1x, p1y))
        l2 = Line(Point(p2x, p2y), Point(p3x, p3y))
        if isPararell(l1, l2):
            print(2)
        elif isVertical(l1, l2):
            print(1)
        else:
            print(0)

def verify_2B():
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y in Query:
        s1 = Segment(Point(p0x, p0y), Point(p1x, p1y))
        s2 = Segment(Point(p2x, p2y), Point(p3x, p3y))
        if isIntersect_ss(s1, s2):
            print(1)
        else:
            print(0)


def verify_2C():
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y in Query:
        s1 = Segment(Point(p0x, p0y), Point(p1x, p1y))
        s2 = Segment(Point(p2x, p2y), Point(p3x, p3y))
        print(crosspoint_ss(s1, s2))  

def verify_2D():
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y in Query:
        s1 = Segment(Point(p0x, p0y), Point(p1x, p1y))
        s2 = Segment(Point(p2x, p2y), Point(p3x, p3y))
        print("{:.8f}".format(distance_ss(s1, s2)))

def verify_7A():
    c1x, c1y, c1r = map(int, input().split())
    c2x, c2y, c2r = map(int, input().split())
    print(intersect_cc(Circle(Point(c1x, c1y), c1r), Circle(Point(c2x, c2y), c2r)))

def verify_7D():
    cx, cy, cr = map(int, input().split())
    c = Circle(Point(cx, cy), cr)
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for x1, y1, x2, y2 in Query:
        Points = crosspoint_lc(Line(Point(x1, y1), Point(x2,y2)), c)
        if len(Points) == 1:
            Points.append(Points[-1])
        Points.sort(key=lambda p: p.y)
        Points.sort(key=lambda p: p.x)
        print(*Points)

def verify_7E():
    c1x, c1y, c1r = map(int, input().split())
    c1 = Circle(Point(c1x, c1y), c1r)
    c2x, c2y, c2r = map(int, input().split())
    c2 = Circle(Point(c2x, c2y), c2r)

    Points = crosspoint_cc(c1, c2)
    if len(Points) == 1:
        Points.append(Points[-1])
    Points.sort(key=lambda p: p.y)
    Points.sort(key=lambda p: p.x)
    print(*Points)  

def verify_7F():
    px, py = map(int, input().split())
    cx, cy, cr = map(int, input().split())
    Points = tangent_cp(Circle(Point(cx, cy), cr), Point(px, py))
    if len(Points) == 1:
        Points.append(Points[-1])
    Points.sort(key=lambda p: p.y)
    Points.sort(key=lambda p: p.x)
    print(*Points, sep="\n")    

verify_7F()
