#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
4 5
0 0 1 0 0
1 0 0 0 0
0 0 0 1 0
0 0 0 1 0

output:
6
"""

import sys


# from collections import namedtuple


class Rectangle(object):
    __slots__ = ('pos', 'height')

    def __init__(self, pos=float('inf'), height=-1):
        """
        init a Rectangle
        """
        self.pos = pos
        self.height = height


def gen_rec_info(_carpet_info):
    dp = [[float('inf')] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if int(_carpet_info[i][j]):
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + 1 if i > 0 else 1

    return dp


def get_largest_area(_hi_info):
    hi_max_area = 0
    rec_stack = []
    _hi_info.append(0)

    for i, v in enumerate(_hi_info):
        rect = Rectangle(pos=i, height=int(v))
        if not rec_stack:
            rec_stack.append(rect)
        else:
            last_height = rec_stack[-1].height
            if last_height < rect.height:
                rec_stack.append(rect)
            elif last_height > rect.height:
                target = i
                while rec_stack and rec_stack[-1].height >= rect.height:
                    pre = rec_stack.pop()
                    area = pre.height * (i - pre.pos)
                    hi_max_area = max(hi_max_area, area)
                    target = pre.pos
                rect.pos = target
                rec_stack.append(rect)

    return hi_max_area


def solve(_rec_info):
    overall_max_area = 0
    for hi_info in _rec_info:
        overall_max_area = max(overall_max_area, get_largest_area(hi_info))

    return overall_max_area


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    H, W = map(int, _input[0].split())
    carpet_info = list(map(lambda x: x.split(), _input[1:]))
    # Rectangle = namedtuple('Rectangle', ('pos', 'height'))

    rec_info = gen_rec_info(carpet_info)
    # print(rec_info)
    ans = solve(rec_info)
    print(ans)