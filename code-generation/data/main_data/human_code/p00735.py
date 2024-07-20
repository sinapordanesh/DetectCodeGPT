#!/usr/bin/env python
# -*- coding: utf-8 -*-

def monsat(num):
    L = [False for i in range(num+1)]
    for i in range(0,num,7):
        if i == 1 or i == 0:
            continue
        for d in [-1,1]:
            if L[i+d] == False:
                L[i+d] = True
                for j in range((i+d)*2,num,i+d):
                    if L[j] is False:
                        L[j] = [i+d]
                    else:
                        L[j].append(i+d)
    return L

L = monsat(3*10**5+1)
while True:
    n = int(input())
    if n == 1:
        break
    print(str(n) + ':',n if L[n] is True else ' '.join(map(str,L[n])))