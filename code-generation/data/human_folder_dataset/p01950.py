from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, readline().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    cnts = [1, 0]
    dist = [[-1]*N for i in range(2)]
    dist[0][0] = 0
    que = deque([(0, 0)])
    while que:
        v, t = que.popleft()
        t1 = t^1
        dist1 = dist[t^1]
        d1 = dist[t][v]+1
        for w in G[v]:
            if dist1[w] != -1:
                continue
            dist1[w] = d1
            que.append((w, t1))
            cnts[t1] += 1
            if cnts[t1] == N:
                write("%d\n" % d1)
                break
        else:
            continue
        break
    else:
        write("-1\n")
solve()
