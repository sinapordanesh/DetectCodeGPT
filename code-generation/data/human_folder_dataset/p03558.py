import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    k = int(input())
    dist = [INF] * k
    dist[1] = 1
    queue = [1]

    for v in queue:
        tmp = [v]
        for v in tmp:
            if dist[10 * v % k] > dist[v]:
                dist[10 * v % k] = dist[v]
                tmp.append(10 * v % k)
            if dist[(v + 1) % k] > dist[v] + 1:
                dist[(v + 1) % k] = dist[v] + 1
                queue.append((v + 1) % k)

    print(dist[0])
resolve()