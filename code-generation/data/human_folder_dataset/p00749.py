#2006_D
"""
import sys
from collections import defaultdict
def dfs(d,y,x,f):
    global ans
    if d >= 10:
        return
    f_ = defaultdict(int)
    for i in f.keys():
        f_[i] = f[i]
    for t,s in vr[(y,x)]:
        if a[t][s] == 3:
            ans = min(ans,d+1)
            break
        elif f[(t,s)]:
            if s == x+1:
                break
            f_[(t,s)] = 0
            dfs(d+1,t,s-1,f_)
            f_[(t,s)] = 1
            break

    for t,s in vl[(y,x)]:
        if a[t][s] == 3:
            ans = min(ans,d+1)
            break
        elif f[(t,s)]:
            if s == x-1:
                break
            f_[(t,s)] = 0
            dfs(d+1,t,s+1,f_)
            f_[(t,s)] = 1
            break

    for t,s in vd[(y,x)]:
        if a[t][s] == 3:
            ans = min(ans,d+1)
            break
        elif f[(t,s)]:
            if t == y+1:
                break
            f_[(t,s)] = 0
            dfs(d+1,t-1,s,f_)
            f_[(t,s)] = 1
            break

    for t,s in vu[(y,x)]:
        if a[t][s] == 3:
            ans = min(ans,d+1)
            break
        elif f[(t,s)]:
            if t == y-1:
                break
            f_[(t,s)] = 0
            dfs(d+1,t+1,s,f_)
            f_[(t,s)] = 1
            break
    return
while 1:
    w,h = map(int, sys.stdin.readline()[:-1].split())
    if w == h == 0:
        break
    a = [list(map(int, sys.stdin.readline()[:-1].split())) for i in range(h)]
    vr = defaultdict(list)
    vl = defaultdict(list)
    vd = defaultdict(list)
    vu = defaultdict(list)
    f = defaultdict(int)
    for y in range(h):
        for x in range(w):
            if a[y][x] == 1:
                f[(y,x)] = 1
            if a[y][x] in [1,3]:
                for x_ in range(x):
                    vr[(y,x_)].append((y,x))
            elif a[y][x] == 2:
                sy,sx = y,x
    for y in range(h):
        for x in range(w)[::-1]:
            if a[y][x] in (1,3):
                for x_ in range(x+1,w):
                    vl[(y,x_)].append((y,x))
    for x in range(w):
        for y in range(h):
            if a[y][x] in (1,3):
                for y_ in range(y):
                    vd[(y_,x)].append((y,x))
    for x in range(w):
        for y in range(h)[::-1]:
            if a[y][x] in (1,3):
                for y_ in range(y+1,h):
                    vu[(y_,x)].append((y,x))
    ind = [[[0]*4 for i in range(w)] for j in range(h)]
    ans = 11
    dfs(0,sy,sx,f)
    ans = ans if ans < 11 else -1
    print(ans)
"""

#2018_D
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

def dfs(d,s,l,v,dic):
    s_ = tuple(s)
    if dic[(d,s_)] != None:
        return dic[(d,s_)]
    if d == l:
        dic[(d,s_)] = 1
        for x in s:
            if x > (n>>1):
                dic[(d,s_)] = 0
                return 0
        return 1
    else:
        res = 0
        i,j = v[d]
        if s[i] < (n>>1):
            s[i] += 1
            res += dfs(d+1,s,l,v,dic)
            s[i] -= 1
        if s[j] < (n>>1):
            s[j] += 1
            res += dfs(d+1,s,l,v,dic)
            s[j] -= 1
        dic[(d,s_)] = res
        return res

def solve(n):
    dic = defaultdict(lambda : None)
    m = int(sys.stdin.readline())
    s = [0]*n
    f = [[1]*n for i in range(n)]
    for i in range(n):
        f[i][i] = 0
    for i in range(m):
        x,y = [int(x) for x in sys.stdin.readline().split()]
        x -= 1
        y -= 1
        s[x] += 1
        f[x][y] = 0
        f[y][x] = 0
    v = []
    for i in range(n):
        for j in range(i+1,n):
            if f[i][j]:
                v.append((i,j))
    l = len(v)
    print(dfs(0,s,l,v,dic))

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    solve(n)
"""
#2011_D
"""
import sys
def dfs(s,d,f,v):
    global ans
    if ans == n-n%2:
        return
    if d > ans:
        ans = d
    for i in range(n):
        if s[i] == 0:
            for j in range(i+1,n):
                if s[j] == 0:
                    if f[i] == f[j]:
                        s[i] = -1
                        s[j] = -1
                        for k in v[i]:
                            s[k] -= 1
                        for k in v[j]:
                            s[k] -= 1
                        dfs(s,d+2,f,v)
                        s[i] = 0
                        s[j] = 0
                        for k in v[i]:
                            s[k] += 1
                        for k in v[j]:
                            s[k] += 1

def solve(n):
    p = [[int(x) for x in sys.stdin.readline().split()] for i in range(n)]
    v = [[] for i in range(n)]
    f = [0]*n
    s = [0]*n
    for i in range(n):
        x,y,r,f[i] = p[i]
        for j in range(i+1,n):
            xj,yj,rj,c = p[j]
            if (x-xj)**2+(y-yj)**2 < (r+rj)**2:
                v[i].append(j)
                s[j] += 1
    dfs(s,0,f,v)
    print(ans)
while 1:
    n = int(sys.stdin.readline())
    ans = 0
    if n == 0:
        break
    solve(n)
"""

#2003_D
"""
import sys
def root(x,par):
    if par[x] == x:
        return x
    par[x] = root(par[x],par)
    return par[x]

def unite(x,y,par,rank):
    x = root(x,par)
    y = root(y,par)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def solve(n):
    p = [[float(x) for x in sys.stdin.readline().split()] for i in range(n)]
    v = []
    for i in range(n):
        for j in range(i):
            xi,yi,zi,ri = p[i]
            xj,yj,zj,rj = p[j]
            d = max(0,((xi-xj)**2+(yi-yj)**2+(zi-zj)**2)**0.5-(ri+rj))
            v.append((i,j,d))
    par = [i for i in range(n)]
    rank = [0]*n
    v.sort(key = lambda x:x[2])
    ans = 0
    for x,y,d in v:
        if root(x,par) != root(y,par):
            unite(x,y,par,rank)
            ans += d
    print("{:.3f}".format(round(ans,3)))

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    solve(n)
"""

#2009_D
"""
import sys
from heapq import heappop,heappush
from collections import defaultdict
def solve(n,m):
    s,g = [int(x) for x in sys.stdin.readline().split()]
    s -= 1
    g -= 1
    e = [[] for i in range(n)]
    for i in range(m):
        a,b,d,c = [int(x) for x in sys.stdin.readline().split()]
        a -= 1
        b -= 1
        e[a].append((b,d,c))
        e[b].append((a,d,c))
    dist = defaultdict(lambda : float("inf"))
    dist[(s,0,-1)] = 0
    q = [(0,s,0,-1)]
    while q:
        dx,x,v,p = heappop(q)
        if x == g and v == 1:
            print(dx)
            return
        for i in range(-1,2):
            v_ = v+i
            if v_ < 1 :continue
            for y,d,c in e[x]:
                if p == y:
                    continue
                if v_ > c:
                    continue
                z = d/v_
                if dx+z < dist[(y,v_,x)]:
                    dist[(y,v_,x)] = dx+z
                    heappush(q,(dist[(y,v_,x)],y,v_,x))
    print("unreachable")
    return

while 1:
    n,m = [int(x) for x in sys.stdin.readline().split()]
    if n == 0:
        break
    solve(n,m)
"""

#2016_D
"""
import sys
def solve(n):
    w = [int(x) for x in sys.stdin.readline().split()]
    dp = [[0]*(n+1) for i in range(n+1)]
    for le in range(n+1):
        for l in range(n):
            r = l+le
            if r > n:break
            if not (r-l)%2 and abs(w[l]-w[r-1]) < 2:
                if dp[l+1][r-1] == r-l-2:
                    dp[l][r] = r-l
                    continue
            for k in range(l+1,r):
                if dp[l][k] + dp[k][r] > dp[l][r]:
                    dp[l][r] = dp[l][k] + dp[k][r]
    print(dp[0][n])
while 1:
    n = int(sys.stdin.readline())
    if not n:
        break
    solve(n)
"""
#2009_D
"""
alp = list("abcdefghijklmnopqrstuvwxyz")
c = {}
key = {}
for i in range(25):
    c[alp[i]] = alp[i+1]
    key[alp[i]] = i
key["z"] = 25

def dfs(i,k,f,n):
    global ans
    if i == n:
        for j in k:
            if f[key[j]]:
                break
        else:
            ans.append(k)
    else:
        dfs(i+1,k+s[i],f,n)
        if s[i] != "z" and f[key[s[i]]+1]:
            f[key[s[i]]+1] = 0
            dfs(i+1,k+c[s[i]],f,n)
            f[key[s[i]]+1] = 1

def solve(s):
    global ans
    n = len(s)
    d = {}
    for i in s:
        d[i] = 1
    f = [1]*26
    f[0] = 0
    dfs(0,"",f,n)
    ans.sort()
    print(len(ans))
    if len(ans) < 10:
        for i in ans:
            print(i)
    else:
        for i in ans[:5]:
            print(i)
        for i in ans[-5:]:
            print(i)
while 1:
    s = input()
    ans = []
    if s == "#":
        break
    solve(s)
"""

#2004_D
"""
import sys
from collections import defaultdict
while 1:
    d = defaultdict(list)
    d_ = defaultdict(list)
    n = int(sys.stdin.readline())
    if n == 0:break
    point = [[float(x) for x in sys.stdin.readline().split()] for i in range(n)]
    ans = 1
    for i in range(n):
        p,q = point[i]
        for j in range(n):
            if i == j:continue
            s,t = point[j]
            if (p-s)**2+(q-t)**2 > 4:
                continue
            d[i].append(j)
            if j > i:
                d_[i].append(j)

    for i in range(n):
        p,q = point[i]
        for j in d_[i]:
            s,t = point[j]
            v = (t-q,p-s)
            m = ((p+s)/2,(q+t)/2)
            l = 0
            r = 10000
            while r-l > 0.0001:
                k = (l+r)/2
                a,b = m[0]+k*v[0],m[1]+k*v[1]
                if (p-a)**2+(q-b)**2 < 1:
                    l = k
                else:
                    r = k
            ans_ = 2
            for l in d[i]:
                if l == j:
                    continue
                x,y = point[l]
                if (x-a)**2+(y-b)**2 < 1:
                    ans_ += 1

            if ans_ > ans:
                ans = ans_
                if ans == n:break

            k = -k
            a,b = m[0]+k*v[0],m[1]+k*v[1]
            ans_ = 2
            for l in d[i]:
                if l == j:
                    continue
                x,y = point[l]
                if (x-a)**2+(y-b)**2 < 1:
                    ans_ += 1

            if ans_ > ans:
                ans = ans_
                if ans == n:break
        if ans == n:break
    print(ans)
"""
#2010_D
import sys
from collections import defaultdict,deque
d = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(b,a,k):
    q = deque([(b,a)])
    bfs_map[b][a] = k
    g = a+0.5
    p = s[b][a]
    su = 1
    while q:
        y,x = q.popleft()
        for dy,dx in d:
            y_ = y+dy
            x_ = x+dx
            if 0 <= y_ < h and 0 <= x_ < w:
                if bfs_map[y_][x_] < 0 and s[y_][x_] == p:
                    bfs_map[y_][x_] = k
                    q.append((y_,x_))
                    g += x_+0.5
                    su += 1
    f[k] = (g,su)

def dfs(x):
    if g[x] != None:
        return g[x]
    g[x] = [f[x][0],f[x][1]]
    for y in v[x]:
        g_ = dfs(y)
        g[x][0] += g_[0]
        g[x][1] += g_[1]
    return g[x]

while 1:
    w,h = [int(x) for x in sys.stdin.readline().split()]
    if w == 0:
        break
    s = [sys.stdin.readline()[:-1] for i in range(h)]
    f = defaultdict(lambda : 0)
    bfs_map = [[-1]*w for i in range(h)]
    k = 0
    for y in range(h)[::-1]:
        for x in range(w):
            if s[y][x] != "." and bfs_map[y][x] < 0:
                bfs(y,x,k)
                k += 1

    v = [[] for i in range(k)]
    l = [float("inf")]*k
    r = [0]*k
    fl = [1]*k

    for y in range(h):
        for x in range(w):
            if bfs_map[y][x] > -1:
                b = bfs_map[y][x]
                if y == h-1 or (bfs_map[y+1][x] != b and bfs_map[y+1][x] > -1):
                    l[b] = min(l[b],x)
                    r[b] = max(r[b],x+1)
                    if y < h-1 and fl[b]:
                        v[bfs_map[y+1][x]].append(b)
                        fl[b] = 0
    g = [None]*k
    for i in range(k):
        dfs(i)
        gx = g[i][0]/g[i][1]
        if gx <= l[i] or r[i] <= gx:
            print("UNSTABLE")
            break
    else:
        print("STABLE")

