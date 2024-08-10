#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	set_union
# CreatedDate:  2020-06-09 16:02:02 +0900
# LastModified: 2020-06-09 16:04:20 +0900
#


import os
import sys
#import numpy as np
#import pandas as pd


def main():
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))
    c=a+b
    c=list(set(c))
    c.sort()
    for ab in c:
        print(ab)


if __name__ == "__main__":
    main()

