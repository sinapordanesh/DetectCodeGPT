import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
import bisect
from functools import reduce

def main():
    H, N = MI()
    A = LI()
    A_sum = sum(A)
    if A_sum >= H:
        print('Yes')
    else:
        print('No')



if __name__ == "__main__":
    main()

