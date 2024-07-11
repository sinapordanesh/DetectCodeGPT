from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    INF = 10**9
    A = tuple(map(int, readline().split()))
    B = tuple(range(1, N+1))
    def check(N, A, N1):
        que = [(0, A)]
        dist = {A: 0}
        S = [A]
        B = list(A)
        for cost in range(N1):
            T = []
            for v in S:
                if dist[v] < cost:
                    continue
                for i in range(N):
                    B[:] = v
                    for j in range(i+1, N):
                        B[i:j+1] = reversed(v[i:j+1])
                        key = tuple(B)
                        if cost+1 < dist.get(key, N1+1):
                            dist[key] = cost+1
                            T.append(key)
            S = T
        return dist
    D0 = check(N, A, (N-1)//2)
    D1 = check(N, B, (N-1)//2)
    ans = N-1
    for state, v in D0.items():
        if state in D1:
            ans = min(ans, v + D1[state])
    write("%d\n" % ans)
solve()
