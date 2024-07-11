from collections import deque, Counter
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

mod = 10**9 + 7
h, w = map(int, input().split())
n = int(input())

ans = 0

black = []
row = Counter()
column = Counter()
for _ in range(n):
    x, y = map(int, input().split())
    row[x] += 1
    column[y] += 1
    black.append((x, y))
row[h] += 1
column[w] += 1


def sqsum(x):
    return x*(x+1)*(2*x+1)//6


pre = -1
top = 0
bottom = h*w - n
area = []
for i in sorted(row.keys()):
    if i == pre+2:
        top += w
        bottom -= w
        area.append([-1, 1])
    elif i > pre+2:
        ans += (i-pre-2)*top*bottom + ((i-pre-2)*(i-pre-1)//2) * \
            w*(bottom-top) - sqsum(i-pre-2)*(w**2)
        ans %= mod
        top += (i-pre-1)*w
        bottom -= (i-pre-1)*w
        area.append([-1, i-pre-1])
    if i != h:
        top += w-row[i]
        bottom -= w-row[i]
        area.append([i])
    pre = i

R = len(area)

pre = -1
left = 0
right = h*w-n
area2 = []
for j in sorted(column.keys()):
    if j == pre+2:
        left += h
        right -= h
        area2.append([area[i][1] if area[i][0] == -1 else 1 for i in range(R)])
    elif j > pre+2:
        ans += (j-pre-2)*left*right + ((j-pre-2)*(j-pre-1)//2) * \
            h*(right-left) - sqsum(j-pre-2)*(h**2)
        ans %= mod
        left += (j-pre-1)*h
        right -= (j-pre-1)*h
        area2.append([(j-pre-1)*area[i][1] if area[i][0]
                      == -1 else (j-pre-1) for i in range(R)])
    if j != w:
        left += h-column[j]
        right -= h-column[j]
        tmp = []
        for i in range(R):
            if area[i][0] == -1:
                tmp.append(area[i][1])
            else:
                if (area[i][0], j) in black:
                    tmp.append(0)
                else:
                    tmp.append(1)
        area2.append(tmp)
    pre = j


C = len(area2)
area2 = [[area2[j][i] for j in range(C)] for i in range(R)]

vec = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def bfs(p, q):
    dist = [[10**5 for _ in range(C)] for __ in range(R)]
    visited = [[False for _ in range(C)] for __ in range(R)]
    dist[p][q] = 0
    visited[p][q] = True
    q = deque([(p, q)])
    while q:
        x, y = q.popleft()
        for dx, dy in vec:
            if 0 <= x+dx < R and 0 <= y+dy < C and area2[x+dx][y+dy] != 0:
                if not visited[x+dx][y+dy]:
                    dist[x+dx][y+dy] = dist[x][y] + 1
                    visited[x+dx][y+dy] = True
                    q.append((x+dx, y+dy))
    return dist


ans2 = 0

for x in range(R*C):
    i = x//C
    j = x % C
    if area2[i][j] == 0:
        continue
    d = bfs(i, j)
    for y in range(R*C):
        k = y//C
        l = y % C
        if area2[k][l] == 0:
            continue
        ans2 += area2[i][j]*area2[k][l]*d[k][l]
        ans2 %= mod

ans2 *= pow(2, mod-2, mod)

print((ans+ans2) % mod)
