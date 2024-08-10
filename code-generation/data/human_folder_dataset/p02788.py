import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
from collections import deque
import bisect
from decimal import *
def main():
    N, D, A = MI()
    Enemy = defaultdict()
    Enemy_ran = []
    for i in range(N):
        x, h = MI()
        Enemy[x] = h
        Enemy_ran.append(x)
    Enemy_ran.sort()
    cnt = 0
    dam_list = deque()
    dam_all = 0
    for i in range(N):
        x = Enemy_ran[i]
        while len(dam_list) != 0 and i >= dam_list[0][0]:
            dam_all -= dam_list.popleft()[1]
        HP = Enemy[x] - dam_all
        if HP <= 0:
            continue
        else:
            ata = math.ceil(Decimal(HP) / Decimal(A))
            cnt += ata
            ran = x + 2 * D
            y = bisect.bisect_right(Enemy_ran, ran)
            dam = ata * A
            dam_list.append((y, dam))
            dam_all += dam


    print(cnt)


if __name__ == "__main__":
    main()

