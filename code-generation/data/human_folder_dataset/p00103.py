#!/usr/bin/python3

n = int(input())

def solve():
    o = 0
    s = 0
    b = [False, False, False]
    while o < 3:
        inst = input()
        if inst == 'OUT':
            o += 1
        elif inst == 'HIT':
            if b[2]:
                s += 1
            b2 = [True]
            b2.extend(b[0:2])
            b = b2
        elif inst == 'HOMERUN':
            s += 1
            for k in range(3):
                if b[k]:
                    b[k] = False
                    s += 1
    return s

for _ in range(n):
    print(solve())