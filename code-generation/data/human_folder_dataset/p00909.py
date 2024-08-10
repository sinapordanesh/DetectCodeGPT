import sys
sys.setrecursionlimit(10**6)
def root(x):
    if x == parent[x]:
        return x
    y = root(parent[x])
    relative[x] += relative[parent[x]]
    parent[x] = y
    return y
def unite(a, b, w):
    pa = root(a); pb = root(b)
    pw = relative[a] + w - relative[b]
    if pa < pb:
        parent[pb] = pa
        relative[pb] = pw
    else:
        parent[pa] = pb
        relative[pa] = -pw
while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    *parent, = range(N)
    relative = [0]*N
    for i in range(M):
        cmd = input().split()
        if cmd[0] == '!':
            a, b, w = map(int, cmd[1:])
            unite(a-1, b-1, w)
        else:
            a, b = map(int, cmd[1:])
            if root(a-1) != root(b-1):
                print("UNKNOWN")
            else:
                print(relative[b-1] - relative[a-1])