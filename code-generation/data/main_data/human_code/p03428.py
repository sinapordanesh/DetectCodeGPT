import math
from copy import deepcopy
import sys
input = sys.stdin.readline

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vec(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vec(self.x-other.x, self.y-other.y)

    def __mul__(self, k):
        return Vec(self.x*k, self.y*k)

    def __truediv__(self, k):
        return Vec(self.x/k, self.y/k)

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)

    def abs(self):
        return (self.x**2 + self.y**2)**.5

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def cross(self, other):
        return self.x*other.y - self.y*other.x

    def rot(self, ang):
        c = math.cos(ang)
        s = math.sin(ang)
        return Vec(c*self.x-s*self.y, s*self.x+c*self.y)

    def arg(self):
        return math.atan2(self.y, self.x)


def convex_hull(points, eps=1e-12):
    n = len(points)
    points.sort(key=lambda p: (p.x, p.y))
    k = 0  # # of vertices in the convex hull
    ch = [None] * (2*n)
    # bottom
    for i in range(n):
        while k > 1 and (ch[k-1]-ch[k-2]).cross(points[i]-ch[k-1]) < eps:
            k -= 1
        ch[k] = points[i]
        k += 1
    t = k
    # top
    for i in range(0, n-1)[::-1]:
        while k > t and (ch[k-1]-ch[k-2]).cross(points[i]-ch[k-1]) < eps:
            k -= 1
        ch[k] = points[i]
        k += 1
    return ch[:k-1]


N = int(input())
points = [Vec(*map(int, input().split())) for _ in range(N)]
tmp = deepcopy(points)
ch = convex_hull(tmp)
ch.sort(key=lambda v: v.arg())
ans = [0] * N
for i in range(len(ch)):
    p0 = ch[(i-1) % len(ch)]
    p1 = ch[i]
    p2 = ch[(i+1) % len(ch)]
    a = (p2 - p1).arg() - (p1 - p0).arg()
    if a < 0:
        a += 2 * math.pi
    for j in range(N):
        if p1 == points[j]:
            ans[j] = a / (2 * math.pi)
print(*ans, sep='\n')