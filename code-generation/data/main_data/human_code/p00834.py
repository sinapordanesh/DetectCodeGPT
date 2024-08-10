from collections import defaultdict, deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    if N == 0:
        return False
    C0 = [list(map(int, readline().split())) for i in range(N)]
    U = [1]*N
    D = defaultdict(list)
    for i in range(N):
        xi, yi, zi, ri = C0[i]
        for j in range(i):
            xj, yj, zj, rj = C0[j]
            dd = (xi - xj)**2 + (yi - yj)**2 + (zi - zj)**2
            if dd <= (ri - rj)**2:
                if ri < rj:
                    U[i] = 0
                else:
                    U[j] = 0
    C = [e for i, e in enumerate(C0) if U[i]]
    N = len(C)
    EPS = 1e-9
    for i in range(N):
        xi, yi, zi, ri = C[i]
        D[zi+ri].append((0, i, 0))
        D[zi-ri].append((0, i, 0))
        for j in range(i):
            xj, yj, zj, rj = C[j]
            dd = (xi - xj)**2 + (yi - yj)**2 + (zi - zj)**2
            if dd > (ri + rj)**2:
                continue
            def check(z):
                si = (ri**2 - (z - zi)**2)**.5
                sj = (rj**2 - (z - zj)**2)**.5
                return (xi - xj)**2 + (yi - yj)**2 <= (si + sj)**2
            z0 = zi + (zj - zi) * (ri**2 + dd - rj**2) / (2 * dd)
            zm = min(zi+ri, zj+rj)
            if check(zm):
                z1 = zm
            else:
                left = 0; right = zm - z0
                while right - left > EPS:
                    mid = (left + right) / 2
                    # xi, yi, sqrt(ri**2 - (mid - zi)**2)
                    if check(z0 + mid):
                        left = mid
                    else:
                        right = mid
                z1 = z0 + left
            zm = max(zi-ri, zj-rj)
            if check(zm):
                z2 = zm
            else:
                left = 0; right = z0 - max(zi-ri, zj-rj)
                while right - left > EPS:
                    mid = (left + right) / 2
                    # xi, yi, sqrt(ri**2 - (mid - zi)**2)
                    if check(z0 - mid):
                        left = mid
                    else:
                        right = mid
                z2 = z0 - left
            D[z1].append((1, i, j))
            D[z2].append((1, i, j))

    res = [0]
    E = [[0]*N for i in range(N)]
    U = [0]*N
    *zs, = D.items()
    zs.sort()
    for z, es in zs:
        for t, a, b in es:
            if t:
                E[a][b] = E[b][a] = E[a][b] ^ 1
            else:
                U[a] ^= 1
        c = 0
        que = deque()
        used = [0]*N
        for i in range(N):
            if used[i] or not U[i]:
                continue
            c += 1
            v = 0
            used[i] = 1
            que.append(i)
            while que:
                v = que.popleft()
                for w in range(N):
                    if not E[v][w] or used[w]:
                        continue
                    used[w] = 1
                    que.append(w)
        if res[-1] != c:
            res.append(c)
    ans = []
    for i in range(len(res)-1):
        if res[i] < res[i+1]:
            ans.append("1")
        else:
            ans.append("0")
    write("%d\n" % len(ans))
    write("".join(ans))
    write("\n")
    return True
while solve():
    ...
