import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N = int(readline())
    if N == 0:
        return False
    P = [list(map(int, readline().split())) for i in range(N)]
    L = 2000
    Q = [[] for i in range(2*L+1)]
    LS = []
    for i in range(N):
        x0, y0 = P[i-1]; x1, y1 = P[i]
        if y0 != y1:
            Q[y0].append(i); Q[y1].append(i)
        LS.append((P[i-1], P[i]) if y0 < y1 else (P[i], P[i-1]))
    U = [0]*N
    s = set()
    ans = 0
    for y in range(-L, L):
        for i in Q[y]:
            if U[i]:
                s.remove(i)
            else:
                s.add(i)
                U[i] = 1
        *js, = s
        def f(i):
            (x0, y0), (x1, y1) = LS[i]
            dx = x1 - x0; dy = y1 - y0
            if dx < 0:
                return (x0 + dx*((y+1) - y0)/dy, x0 + (dx*(y - y0) + dy-1)//dy)
            return (x0 + dx*(y - y0)/dy, x0 + (dx*((y+1) - y0) + dy-1)//dy)
        js.sort(key = f)
        l = r = -5000

        for k, i in enumerate(js):
            (x0, y0), (x1, y1) = LS[i]
            dx = x1 - x0; dy = y1 - y0
            if k & 1:
                if dx >= 0:
                    x = x0 + (dx*((y+1) - y0) + dy-1) // dy
                else:
                    x = x0 + (dx*(y - y0) + dy-1) // dy
                r = x
            else:
                if dx >= 0:
                    x = x0 + dx*(y - y0) // dy
                else:
                    x = x0 + dx*((y+1) - y0) // dy
                if r < x:
                    ans += r-l
                    l = x
        ans += r-l
    write("%d\n" % ans)
    return True
while solve():
    ...
