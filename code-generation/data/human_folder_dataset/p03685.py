from collections import deque

def f(x, y):
    if x == 0:
        return y
    if y == 0:
        return -x
    if x == r:
        return -(x + y)
    if y == c:
        return x + y

r, c, n = map(int, input().split())
xy = []
lxy = 0
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    d = []
    if min(x1, y1) == 0 or x1 == r or y1 == c:
        d.append([f(x1, y1), i])
    if min(x2, y2) == 0 or x2 == r or y2 == c:
        d.append([f(x2, y2), i])
    if len(d) == 2:
        xy.append(d[0])
        xy.append(d[1])
        lxy += 2
xy.sort()
q = deque()
lq = -1
for i in range(lxy):
    if not q:
        q.append(xy[i][1])
        lq += 1
    else:
        if q[lq] == xy[i][1]:
            q.pop()
            lq -= 1
        else:
            q.append(xy[i][1])
            lq += 1
print("YES" if not q else "NO")