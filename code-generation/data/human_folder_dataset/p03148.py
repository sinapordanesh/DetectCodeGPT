from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,k = inpl()
sushis = [] #[美味しさ,種類]
for _ in range(n):
    a,b = inpl()
    sushis.append([b,a])
sushis.sort(reverse = True)
sushis = deque(sushis)
cnt = [0] * (n+1)
kind = 0
ois_sum = 0
eats = []
for i in range(k):
    ois,knd = sushis.popleft()
    if cnt[knd] == 0:
        kind += 1
    cnt[knd] += 1
    ois_sum += ois
    eats.append([ois,knd])
eats.sort()
res = ois_sum + kind**2
ind = 0
while sushis and ind < k:
    while ind < k:
        eat_knd = eats[ind][1]
        if cnt[eat_knd] <= 1: 
            ind += 1
        else: break
    if ind >= k: break
    ois,knd = sushis.popleft()
    if cnt[knd]: continue
    eat_ois,eat_knd = eats[ind]
    cnt[knd] += 1; cnt[eat_knd] -= 1
    ois_sum -= eat_ois - ois
    kind += 1
    res = max(res, ois_sum + kind**2)
    ind += 1
print(res)
