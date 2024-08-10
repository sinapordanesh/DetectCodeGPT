#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):
        if serial >= sqrt:
            return input_list
        for s in range(serial ** 2, num, serial): 
            input_list[s] = False

primeTable = sieve_of_erastosthenes(13*(10**5))

while True:
    k = int(input())
    if k == 0:
        break
    if primeTable[k]:
        print(0)
    else:
        i = k
        while primeTable[i] is False: i += 1
        j = i-1
        while primeTable[j] is False: j -= 1
        print(i-j)