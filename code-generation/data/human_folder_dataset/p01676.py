from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M = map(int, readline().split())
    G = [[] for i in range(N)]
    for i in range(M):
        s, t = map(int, readline().split())
        G[s-1].append(t-1)

    used = [0]*N
    cnt = 0
    ans = 0
    for i in range(N):
        if used[i]:
            continue
        que = deque([i])
        used[i] = 1
        while que:
            v = que.popleft()
            ans += len(G[v])-1
            for w in G[v]:
                if used[w]:
                    continue
                used[w] = 1
                que.append(w)
        ans += 1
    write("%d\n" % ans)
solve()

