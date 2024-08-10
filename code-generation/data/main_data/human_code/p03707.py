import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m,q = list(map(int, input().split()))
s = [None]*n
for i in range(n):
    s[i] = list(map(int, input()))
e1 = [[0]*(m) for _ in range(n-1)]
e2 = [[0]*(m-1) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i<n-1 and s[i][j]==s[i+1][j]==1:
            e1[i][j] = 1
        if j<m-1 and s[i][j]==s[i][j+1]==1:
            e2[i][j] = 1
def cumsum2(v):
    # v: h*wの2次元リスト
    h,w = len(v), len(v[0])
    v.insert(0, [0]*w)
    for l in v:
        l.insert(0, 0)
    for i in range(1,h+1):
        for j in range(1,w+1):
            v[i][j] = v[i-1][j] + v[i][j-1] - v[i-1][j-1] + v[i][j]
    return v
s = cumsum2(s)
if e1:
    e1 = cumsum2(e1)
if e2:
    e2 = cumsum2(e2)
ans = [None]*q
for i in range(q):
    x1,y1,x2,y2 = map(lambda x: int(x)-1, input().split())
    val = s[x2+1][y2+1] - s[x1][y2+1] - s[x2+1][y1] + s[x1][y1]
    if e1:
        val2 = e1[x2][y2+1] - e1[x2][y1] - e1[x1][y2+1] + e1[x1][y1]
    else:
        val2 = 0
    if e2:
        val3 = e2[x2+1][y2] - e2[x2+1][y1] - e2[x1][y2] + e2[x1][y1]
    else:
        val3 = 0
    ans[i] = val - (val2+val3)
write("\n".join(map(str, ans)))