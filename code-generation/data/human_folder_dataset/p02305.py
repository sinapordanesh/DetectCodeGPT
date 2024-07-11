#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
input:
1 2 1
4 2 2

output:
3
"""

import sys
from collections import namedtuple


class CircleIntersections(object):
    def __init__(self, ):
        _input = sys.stdin.readlines()
        x1, y1, r1 = map(int, _input[0].split())
        x2, y2, r2 = map(int, _input[1].split())

        Circle = namedtuple('Circle', ('centre', 'radius'))
        self.c1 = Circle(centre=x1 + y1 * 1j, radius=r1)
        self.c2 = Circle(centre=x2 + y2 * 1j, radius=r2)

    def calc_intersection(self):
        c_distance = abs(self.c2.centre - self.c1.centre)
        r1, r2 = self.c1.radius, self.c2.radius

        if c_distance > r1 + r2:
            return 4
        elif c_distance == r1 + r2:
            return 3
        elif abs(r1 - r2) < c_distance < r1 + r2:
            return 2
        elif c_distance == abs(r1 - r2):
            return 1
        else:
            return 0


if __name__ == '__main__':
    case = CircleIntersections()
    print(case.calc_intersection())