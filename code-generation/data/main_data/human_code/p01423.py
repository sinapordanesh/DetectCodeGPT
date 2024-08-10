from itertools import product
def main():
    INF = 10**9
    N, M = map(int, input().split())
    E = [[INF]*N for i in range(N)]
    G = [set() for i in range(N)]
    D = [0]*N
    for i in range(M):
        u, v, f = map(int, input().split()); u -= 1; v -= 1
        E[u][v] = E[v][u] = f
        G[u].add(v)
        G[v].add(u)
        D[u] += 1; D[v] += 1

    def calc(vs):
        if len(vs) == 1:
            return 0
        res = 0
        for ps in product([0, 1], repeat=len(vs)):
            R = [v for p, v in zip(ps, vs) if p]
            if len(R) == 1:
                continue
            rs = 0
            for v in R:
                r = INF
                for w in R:
                    if v == w:
                        continue
                    r = min(r, E[v][w])
                rs += r
            res = max(res, rs)
        return res

    def dfs(V, P, X):
        if not P and not X:
            return calc(V)
        u = next(iter(X or P))
        r = 0
        for v in P - G[u]:
            r = max(r, dfs(V | {v}, P & G[v], X & G[v]))
            P.remove(v)
            X.add(v)
        return r

    *I, = range(N)
    I.sort(key = D.__getitem__, reverse=1)

    ans = 0
    P = set(range(N))
    X = set()
    for v in I:
        ans = max(ans,  dfs({v}, P & G[v], X & G[v]))
        P.remove(v)
        X.add(v)
    print(ans)
main()

