from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M = map(int, readline().split())
    if N == M == 0:
        return False
    G = [[] for i in range(N)]
    cs = [0]*N
    for i in range(M):
        u, v = map(int, readline().split())
        forward = [v-1, 1, None]
        backward = forward[2] = [u-1, 0, forward]

        G[u-1].append(forward)
        G[v-1].append(backward)
        cs[v-1] += 1
    prv = [0]*N
    while 1:
        que = deque()
        used = [0]*N
        mi = min(cs); ma = max(cs)
        for i in range(N):
            if mi < cs[i]:
                continue
            que.append(i)
            used[i] = 1
            prv[i] = None
        j = -1
        while que:
            v = que.popleft()
            if mi+2 <= cs[v]:
                j = v
                break
            for w, d, rev in G[v]:
                if d and not used[w]:
                    que.append(w)
                    prv[w] = rev
                    used[w] = 1
        if j == -1:
            break
        v = j
        while prv[v] is not None:
            e = prv[v]
            e[1] = 1; e[2][1] = 0
            v = prv[v][0]
        cs[v] += 1; cs[j] -= 1

    while 1:
        que = deque()
        used = [0]*N
        mi = min(cs); ma = max(cs)
        for i in range(N):
            if cs[i] < ma:
                continue
            que.append(i)
            used[i] = 1
            prv[i] = None
        j = -1
        while que:
            v = que.popleft()
            if cs[v] <= ma-2:
                j = v
                break
            for w, d, rev in G[v]:
                if not d and not used[w]:
                    que.append(w)
                    prv[w] = rev
                    used[w] = 1
        if j == -1:
            break
        v = j
        while prv[v] is not None:
            e = prv[v]
            e[1] = 0; e[2][1] = 1
            v = prv[v][0]
        cs[v] -= 1; cs[j] += 1

    write("%d %d\n" % (min(cs), max(cs)))

    return True
while solve():
    ...
