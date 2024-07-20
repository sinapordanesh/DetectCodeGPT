#!/usr/bin/python3

from decimal import Decimal
from fractions import Fraction
import math
import os
import sys


def main():
    N = read_int()
    A = [Vec(*read_ints()) for _ in range(N)]
    print(*solve(N, A), sep='\n')


def solve(N, Points):
    if DEBUG:
        dprint('polygon({!r}, fill=False)'.format([(v.x, v.y) for v in Points]))

    total_area_2 = 0
    for i in range(1, N - 1):
        a = Points[i] - Points[0]
        b = Points[i + 1] - Points[i]
        total_area_2 += a.cross(b)

    total_area_4 = 0
    bi = -1
    for i in range(1, N - 1):
        a = Points[i] - Points[0]
        b = Points[i + 1] - Points[i]
        area_4 = a.cross(b) * 2
        if total_area_4 + area_4 <= total_area_2:
            total_area_4 += area_4
            continue
        rest = total_area_2 - total_area_4
        k = Fraction(total_area_2 - total_area_4, area_4)
        assert 0 <= k < 1

        bi = i
        bk = k
        bv = Points[i] + k * (Points[i + 1] - Points[i])
        dprint('bi =', bi, 'bk =', bk, 'bv =', bv)
        break

    assert bi != -1

    ai = 0
    ak = 0

    maxl = (bv - Points[0]).abs2()
    minl = maxl

    while bi != 0:
        assert 0 <= ak < 1
        assert 0 <= bk < 1

        dprint('***\nai =', ai, 'ak =', ak, 'bi =', bi, 'bk =', bk)
        dprint('minl =', minl, 'maxl =', maxl)

        a0 = Points[ai]
        a1 = Points[(ai + 1) % N]
        b0 = Points[bi]
        b1 = Points[(bi + 1) % N]

        a2 = a0 + ak * (a1 - a0)
        b2 = b0 + bk * (b1 - b0)

        dprint('a0 =', a0, 'a1 =', a1, 'a2 =', a2)
        dprint('b0 =', b0, 'b1 =', b1, 'b2 =', b2)

        al = 1
        cross = (b2 - a1).cross(b1 - b0)
        if cross != 0:
            bl = Fraction((b0 - a2).cross(b2 - a1), cross)
        else:
            bl = 2  # inf
        assert bk < bl
        if bl > 1:
            al = Fraction((b2 - a0).cross(b1 - a2), (a1 - a0).cross(b1 - a2))
            bl = 1

        assert ak < al <= 1
        assert bk < bl <= 1

        a3 = a0 + al * (a1 - a0)
        b3 = b0 + bl * (b1 - b0)
        dprint('a3 =', a3, 'b3 =', b3)

        b3a3 = b3 - a3
        l = b3a3.abs2()
        dprint('l =', l)
        maxl = max(maxl, l)
        minl = min(minl, l)

        ####
        a3a2 = a3 - a2
        b3b2 = b3 - b2
        b2a2 = b2 - a2

        A0 = a3a2.cross(b2a2)
        B0 = b2a2.cross(b3b2)
        aden = A0.denominator if isinstance(A0, Fraction) else 1
        bden = B0.denominator if isinstance(B0, Fraction) else 1
        gden = aden * bden // math.gcd(aden, bden)
        A0 *= gden
        B0 *= gden
        A0 = int(A0)
        B0 = int(B0)
        g = math.gcd(A0, B0)
        A0 //= g
        B0 //= g
        dprint('y = ({}) * x / (({}) - ({}) * x)'.format(A0, B0, B0 - A0))

        if A0 == B0:
            X2 = (a3a2 - b3b2).abs2()
            X1 = -2 * b2a2.dot(a3a2 - b3b2)
            C = b2a2.abs2()
            dprint('L = ({}) * x^2 + ({}) * x + ({})'.format(X2, X1, C))
            x = Fraction(-X1, 2 * X2)
            dprint('x =', x)
            if 0 <= x <= 1:
                l = x * (X1 + x * X2) + C
                dprint('l =', l)
                minl = min(minl, l)
        else:
            X2 = a3a2.abs2()
            X1 = 2 * (-b2a2.dot(a3a2) + Fraction(A0, B0 - A0) * a3a2.dot(b3b2))
            Y2 = b3b2.abs2()
            Y1 = 2 * (b2a2.dot(b3b2) - Fraction(B0, B0 - A0) * a3a2.dot(b3b2))
            L0 = b2a2.abs2()
            def calc_l(x, y):
                return x * (X1 + x * X2) + y * (Y1 + y * Y2) + L0
            A = Fraction(A0, B0 - A0)
            B = Fraction(B0, B0 - A0)
            poly = [-2 * A * A * B * B * Y2,
                    -A * B * (2 * A * Y2 - Y1),
                    0,
                    2 * B * X2 + X1,
                    2 * X2]
            dprint('poly =', poly)
            sols = solve_poly(poly, -B, 1 - B)
            dprint('sols =', sols)
            for sol_low, sol_high in sols:
                x0 = sol_low + B
                x1 = sol_high + B
                y0 = Fraction(-A * B, x0 - B) - A
                y1 = Fraction(-A * B, x1 - B) - A
                l0 = calc_l(x0, y0)
                l1 = calc_l(x1, y1)
                dprint('l0 =', l0, 'l1 =', l1)
                minl = min(minl, l0, l1)
        ####

        ak = al
        bk = bl
        if ak == 1:
            ai = (ai + 1) % N
            ak = 0
        if bk == 1:
            bi = (bi + 1) % N
            bk = 0

    dprint('minl', minl)
    dprint('maxl', maxl)
    if isinstance(minl, Fraction):
        minld = Decimal(minl.numerator) / Decimal(minl.denominator)
    else:
        minld = Decimal(minl)
    if isinstance(maxl, Fraction):
        maxld = Decimal(maxl.numerator) / Decimal(maxl.denominator)
    else:
        maxld = Decimal(maxl)
    return minld.sqrt(), maxld.sqrt()


def sgn(v):
    if v > 0:
        return 1
    if v < 0:
        return -1
    return 0


EPS = Fraction(1, 10 ** 26)


def solve_poly(poly, minx, maxx):
    while poly and poly[-1] == 0:
        del poly[-1]
    if len(poly) <= 1:
        return []
    if len(poly) == 2:
        b, a = poly
        x = Fraction(-b, a)
        if minx <= x <= maxx:
            return [(x, x)]
        return []

    df = []
    for i in range(1, len(poly)):
        df.append(i * poly[i])
    segs = [(minx, None)] + solve_poly(df, minx, maxx) + [(None, maxx)]
    sols = []

    def f(x):
        v = 0
        for i, a in enumerate(poly):
            v += a * (x ** i)
        return v

    for i in range(len(segs) - 1):
        lb = segs[i][0]
        ub = segs[i + 1][1]
        lbs = sgn(f(lb))
        ubs = sgn(f(ub))
        if (lbs >= 0 and ubs >= 0) or (lbs < 0 and ubs < 0):
            continue
        while ub - lb > EPS:
            midf = Fraction(lb + ub, 2)
            mid = Fraction(Decimal(midf.numerator) / Decimal(midf.denominator))
            if not (lb < mid < ub):
                mid = midf
            v = f(mid)
            if v >= 0:
                if lbs >= 0:
                    lb = mid
                else:
                    ub = mid
            else:
                if lbs >= 0:
                    ub = mid
                else:
                    lb = mid
        sols.append((lb, ub))
    return sols


###############################################################################

class Vec(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vec(self.x / scalar, self.y / scalar)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __idiv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(('Vec', self.x, self.y))

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def abs2(self):
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        return math.sqrt(float(self.abs2()))

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Vec({!r}, {!r})'.format(self.x, self.y)


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()

