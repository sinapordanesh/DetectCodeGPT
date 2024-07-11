#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	map_delete
# CreatedDate:  2020-07-15 11:23:30 +0900
# LastModified: 2020-07-15 11:29:50 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    q = int(input())
    dictionary = {}
    for _ in range(q):
        command = list(input().split())
        if command[0] == '0':
            dictionary[command[1]] = int(command[2])
        elif command[0] == '1':
            if command[1] in dictionary.keys():
                print(dictionary[command[1]])
            else:
                print(0)
        else:
            if command[1] in dictionary.keys():
                del dictionary[command[1]]



if __name__ == "__main__":
    main()

