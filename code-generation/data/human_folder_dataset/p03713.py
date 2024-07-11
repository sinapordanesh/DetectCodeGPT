import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**6)
import itertools
import bisect
from collections import Counter,deque
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    h,w = i_map()
    if h%3 == 0 or w%3 == 0: # 綺麗に三等分できるケース
        print(0)
        exit()

    ans = INF
    th = h//2
    for i in range(1,w//2+2):
        tate = i*h
        yoko1 = (w-i)*th
        yoko2 = (w-i)*(h-th)
        M = max(tate,yoko1,yoko2)
        m = min(tate,yoko1,yoko2)
        ans = min(ans,M-m)

        amari = (w-i)//2
        yoko3 = amari*h
        yoko4 = (w-i-amari)*h
        M = max(tate,yoko3,yoko4)
        m = min(tate,yoko3,yoko4)
        ans = min(ans,M-m)

    tw = w//2
    for i in range(1,h//2+2):
        tate = i*w
        yoko1 = (h-i)*tw
        yoko2 = (h-i)*(w-tw)
        M = max(tate,yoko1,yoko2)
        m = min(tate,yoko1,yoko2)
        ans = min(ans,M-m)

        amari = (h-i)//2
        yoko3 = amari*w
        yoko4 = (h-i-amari)*w
        M = max(tate,yoko3,yoko4)
        m = min(tate,yoko3,yoko4)
        ans = min(ans,M-m)

    print(ans)


if __name__=="__main__":
    main()
