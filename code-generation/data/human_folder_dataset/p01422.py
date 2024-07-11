from heapq import heappush, heappop
def solve():
    N = int(input())
    *A, = map(int, input().split())
    M = 2*10**5
    INF = 10**18
    dist = [[INF]*(M+1) for i in range(N+1)]
    que = [(0, 0, 1)]
    while que:
        cost, i, p = heappop(que)
        if i == N:
            break
        if dist[i][p] + 1e-10 < cost:
            continue
        a = A[i]
        for k in range(p, M+1, p):
            d = max(cost, abs(k - a)/a)
            if d < dist[i+1][k]:
                dist[i+1][k] = d
                heappush(que, (d, i+1, k))
    return min(dist[N])
print("%.16f" % solve())
