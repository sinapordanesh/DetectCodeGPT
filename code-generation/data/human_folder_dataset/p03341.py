#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix
# CreatedDate:  2020-09-27 01:13:48 +0900
# LastModified: 2020-09-27 01:29:07 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N = int(input())
    S = input()
    RW_cnt = S.count("W")
    RE_cnt = S.count("E")
    LW_cnt = 0
    LE_cnt = 0
    if S[0] == "W":
        RW_cnt -= 1
        LW_cnt = 1
    else:
        RE_cnt -= 1
        LE_cnt = 1
    ans = RE_cnt
#    print("RW_cnt, RE_cnt, LW_cnt, LE_cnt")
    for i in range(1, N):
        if i == N-1:
            cnt = LW_cnt
        else:
            cnt = LW_cnt + RE_cnt
        if cnt < ans:
            ans = cnt
        if S[i] == "E":
            LE_cnt += 1
            RE_cnt -= 1
        else:
            LW_cnt += 1
            RW_cnt -= 1
#        print(RW_cnt, RE_cnt, LW_cnt, LE_cnt)
    print(ans)


if __name__ == "__main__":
    main()
