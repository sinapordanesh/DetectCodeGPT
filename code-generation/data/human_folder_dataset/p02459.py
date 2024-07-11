#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	map_search
# CreatedDate:  2020-07-15 11:12:11 +0900
# LastModified: 2020-07-15 11:20:15 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    q = int(input())
    dictionary = dict()
    for _ in range(q):
        command = list(input().split())
        if int(command[0]) == 0:
            dictionary[command[1]] = int(command[2])
        else:
            print(dictionary[command[1]])



if __name__ == "__main__":
    main()

