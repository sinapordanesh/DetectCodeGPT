#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rdp_trace(n: int, i: int) -> list:
    def loop(n: int, i: int) -> list:
        if n == 1:
            return []
        if i <= n // 2:
            rval = loop(n // 2, (n // 2) - i + 1)
            rval.append(i)
            return rval
        else:
            rval = loop(n // 2, i - (n // 2))
            rval.append(i)
            return rval
    return loop(2 ** n, i)

def rdp_connect() -> bool:
    global n, i, j
    n, i, j = map(int, input().split())
    if n == i == j == 0:
        return False
    return True

if __name__ == '__main__':
    while rdp_connect():
        rval = []
        for k, lv in zip(range(n), rdp_trace(n, i)):
            if (lv <= (2 ** (k + 1)) // 2):
                if (j <= (2 ** (n - k)) // 2):
                    rval.append('L')
                    j = (2 ** (n - k)) // 2 - j + 1
                else:
                    rval.append('R')
                    j = (2 ** (n - k)) - j + 1
            else:
                if (j <= (2 ** (n - k)) // 2):
                    rval.append('R')
                else:
                    rval.append('L')
                    j = j - (2 ** (n - k)) // 2
        print(''.join(rval))