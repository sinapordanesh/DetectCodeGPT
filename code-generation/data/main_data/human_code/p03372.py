import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, C = mapint()

Xs = []
Vs = []
for _ in range(N):
    x, v = mapint()
    Xs.append(x)
    Vs.append(v)
r_Xs = [C-x for x in Xs[::-1]]
r_Vs = Vs[::-1]

max_neg = []
tmp = 0
maxi = -10**18
for i in range(N):
    x, v = r_Xs[i], r_Vs[i]
    tmp += v
    max_neg.append(max(tmp-x, maxi))
    maxi = max(tmp-x, maxi)

max_pos = []
tmp = 0
maxi = -10**18
for i in range(N):
    x, v = Xs[i], Vs[i]
    tmp += v
    max_pos.append(max(tmp-x, maxi))
    maxi = max(tmp-x, maxi)
ans = 0
for i in range(N):
    x, v = Xs[i], Vs[i]
    if i!=N-1:
        ans = max(ans, max_pos[i], max_pos[i]-x+max_neg[N-i-2])
    else:
        ans = max(ans, max_pos[i])
for i in range(N):
    x, v = r_Xs[i], r_Vs[i]
    if i!=N-1:
        ans = max(ans, max_neg[i], max_neg[i]-x+max_pos[N-i-2])
    else:
        ans = max(ans, max_neg[i])
print(ans)