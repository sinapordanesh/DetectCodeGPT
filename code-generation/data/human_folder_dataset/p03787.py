mod = 1000000007
eps = 10**-9


def main():
    import sys
    from collections import deque
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    seen = [0] * (N+1)
    single = 0
    bipartite = 0
    not_bipartite = 0
    for v0 in range(1, N+1):
        if seen[v0] != 0:
            continue
        flg = 1
        que = deque()
        que.append(v0)
        seen[v0] = 1
        cnt = 0
        while que:
            v = que.popleft()
            cnt += 1
            for u in adj[v]:
                if seen[u] == 0:
                    seen[u] = -seen[v]
                    que.append(u)
                else:
                    if seen[u] == seen[v]:
                        flg = 0
        if cnt == 1:
            single += 1
        else:
            if flg:
                bipartite += 1
            else:
                not_bipartite += 1
    ans = N ** 2 - (N - single) ** 2
    ans += (bipartite + not_bipartite) ** 2
    ans += bipartite ** 2
    print(ans)


if __name__ == '__main__':
    main()
