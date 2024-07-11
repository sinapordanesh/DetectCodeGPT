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
  N,A,B = i_map()
  h = [i_input() for i in range(N)]

  def check(mid,A,B):
    cnt = 0

    for i in h:
      i -= B*mid
      if i <= 0:
        continue
      cnt += math.ceil(i/(A-B))
    if cnt <= mid:
      return True
    else:
      return False

  start = 1
  end = max(h)

  while end - start > 1:
    middle = (end + start)//2
    if check(middle,A,B):
      end = middle
    else:
      start = middle

  print(end)



if __name__=="__main__":
    main()