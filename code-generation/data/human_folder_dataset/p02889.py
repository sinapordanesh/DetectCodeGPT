import sys
import math
import heapq


def input():
    return sys.stdin.readline().rstrip()


def dijkstra(s, n, es, L):
    # n:頂点数, es: 辺uvのコスト
    d = [10 ** 14 + 7] * n
    # 探索リスト
    S = [(0, s)]
    # 優先度付きキューを使うと計算量が少なくなるよ
    heapq.heapify(S)
    used = [False] * n

    d[s] = 0

    while S:
        # 最小コストの頂点を取り出し
        dg, v = heapq.heappop(S)
        if used[v] == True:
            continue
        used[v] = True
        for u, w in es[v]:
            if d[v] % L + w > L:
                cost = d[v] - d[v] % L + L + w
            else:
                cost = d[v] + w

            if d[u] > cost:
                d[u] = cost
                heapq.heappush(S, (d[u], u))

        # print("d", d)
    return d


def main():
    N, M, L = map(int, input().split())

    dp = [[L+2]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] =0
    for i in range(M):
        x, y, z = map(int, input().split())
        if z > L:
            continue

        x = x - 1
        y = y - 1
        dp[x][y] =z
        dp[y][x]=z



    def warshal(ws,n):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    ws[i][j] =min(ws[i][j],ws[i][k]+ws[k][j])
        return ws

    ls =warshal(dp,N)
    for i in range(N):
        for j in range(N):
            if ls[i][j] <=L:
                ls[i][j] =1
            else:
                ls[i][j] =500
    vs = warshal(ls,N)

    Q =int(input())

    for j in range(Q):
        s,t =map(int,input().split())
        ans = vs[s - 1][t - 1] - 1
        if ans >=N:
            print(-1)
        else:
            print(vs[s-1][t-1]-1)





if __name__ == "__main__":
    main()

# \n
