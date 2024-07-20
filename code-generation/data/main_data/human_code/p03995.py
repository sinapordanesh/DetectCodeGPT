import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w = list(map(int, input().split()))
n = int(input())
from collections import defaultdict
mind = [10**15] * h
dw = defaultdict(list)
for i in range(n):
    r,c,a = map(int, input().split())
    r -= 1
    c -= 1
    mind[r] = min(mind[r], a)
    dw[c].append((a,r))
# 0未満になる要素があるか判定
es = [[] for _ in range(h)]
def main():
    ans = True
    for c in range(w):
        if len(dw[c])<=1:
            continue
        dw[c].sort()
        tmp = 0
        for i in range(len(dw[c])-1):
            u = dw[c][i][1]
            v = dw[c][i+1][1]
            val = dw[c][i+1][0] - dw[c][i][0]
            es[u].append((val, v))
            es[v].append((-val, u))
            tmp += val
            if mind[v]<tmp:
                return False
#     print(es)
#     print(dw)
    vals = [None]*h
    for start in range(h):
        if vals[start] is not None:
            continue
        q = [start]
        vals[start] = 0
        l = [(0, mind[start])]
        while q:
            u = q.pop()
            for d,v in es[u]:
                if vals[v] is None:
                    vals[v] = vals[u] + d
                    l.append((vals[v], mind[v]))
                    q.append(v)
                elif vals[v]!=vals[u]+d:
                    return False
        l.sort()
        for i in range(len(l)):
            if l[i][1]<l[i][0]-l[0][0]:
                return False
#     for u in range(h):
#         for d,v in es[u]:
#             if vals[u]+d!=vals[v]:
#                 return False
    return True
ans = main()
if ans:
    print("Yes")
else:
    print("No")