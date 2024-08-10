#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

import itertools
n = inn()
a = inl()
b = inl()
cms = itertools.combinations(list(range(n)),n//2)
mn = BIG
for cm in cms:
    ev = []
    od = []
    for i in range(n):
        if i not in cm:
            ev.append((a[i] if i%2==0 else b[i], i))
        else:
            od.append((a[i] if i%2==1 else b[i], i))
    ev.sort()
    od.sort()
    #ddprint(f"{ev=}")
    #ddprint(f"{od=}")
    p = []
    q = []
    for i in range(n):
        if i%2==0:
            p.append(ev[i//2][1])
            q.append(ev[i//2][0])
        else:
            p.append(od[i//2][1])
            q.append(od[i//2][0])
    #ddprint(f"{cm=}")
    #ddprint(f"{p=}")
    #ddprint(f"{q=}")
    ok = True
    for i in range(n-1):
        if q[i]>q[i+1]:
            ok = False
            break
    if not ok:
        continue
    x = 0
    for i in range(n//2):
        #ddprint(f"{i=}")
        m = p.index(i)
        tmp = p[m]
        for j in range(m,i,-1):
            p[j] = p[j-1]
        p[i] = tmp
        x += m-i
        #ddprint(f"{m=} {p=}")
        m = p.index(n-1-i)
        tmp = p[m]
        for j in range(m,n-1-i):
            p[j] = p[j+1]
        p[n-1-i] = tmp
        x += n-1-i-m
        #ddprint(f"{m=} {p=}")
    #ddprint(f"{x=}")
    mn = min(mn,x)
print(mn if mn<BIG else -1)
