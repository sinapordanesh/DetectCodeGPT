import sys

K = int(input())
X, Y = map(int, input().split())
dest = (X, Y)
ans = 0
path = []


def sign(i):
    return 2*(i > 0)-1


def dist(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


curpos = [0, 0]
if dist(curpos, dest) == K:
    print(1)
    print(X, Y)
    sys.exit()

while dist(curpos, dest) > 2*K:
    ans += 1
    xdiff = abs(curpos[0] - dest[0])
    curpos[0] += min(K, xdiff) * sign(dest[0] - curpos[0])
    curpos[1] += max(0, K - xdiff) * sign(dest[1] - curpos[1])
    path.append((curpos[0], curpos[1]))

if dist(curpos, dest) % 2 == 1:
    if K % 2 == 0:
        print(-1)
        sys.exit()
    ans += 1
    xdiff = abs(curpos[0] - dest[0])
    curpos[0] += min(K, xdiff) * sign(dest[0] - curpos[0])
    curpos[1] += max(0, K - xdiff) * sign(dest[1] - curpos[1])
    path.append((curpos[0], curpos[1]))
d = dist(curpos, dest)
rest = (2*K-d)//2
ans += 1
xdiff = abs(curpos[0] - dest[0])
if xdiff+rest >= K:
    curpos[0] += (K - rest) * sign(dest[0] - curpos[0])
    curpos[1] -= rest * sign(dest[1] - curpos[1])
else:
    curpos[0] += (xdiff+rest) * sign(dest[0]-curpos[0])
    curpos[1] += (K-(xdiff+rest)) * sign(dest[1] - curpos[1])
path.append((curpos[0], curpos[1]))
path.append(dest)
ans += 1
print(ans)
for p in path:
    print(p[0], p[1])
