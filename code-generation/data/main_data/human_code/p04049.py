import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


from collections import defaultdict
n,k = map(int, input().split())
ns = defaultdict(set)
for _ in range(n-1):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    ns[u].add(v)
    ns[v].add(u)
def bfs(start):
    from queue import deque
    q = deque([start])
    seen = [None] * n
    seen[start] = 0
    dist = defaultdict(list)
    dist[0].append(start)
    while q:
        u = q.pop()
        d = seen[u]
        for v in ns[u]:
            if seen[v] is None and v not in done:
                seen[v] = d + 1
                dist[d+1].append(v)
                q.appendleft(v)
    return seen, dist
ans = 0
done = set()
while True:
    start = 0
    while start in done:
        start += 1
    seen, dist1 = bfs(start)
    m = max(item for item in seen if item is not None)
    u = dist1[m][0]
    seen, dist1 = bfs(u)
    mm = max(item for item in seen if item is not None)
    if mm<=k:
        break
    ans += 1
    v = dist1[mm][0]
    seen, dist2 = bfs(v)
    v1 = sum(len(dist1[u]) for u in range(k+1, mm+1))
    v2 = sum(len(dist2[u]) for u in range(k+1, mm+1))
    if v1<v2:
        done.add(v)
    else:
        done.add(u)
print(ans)