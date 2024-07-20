from functools import reduce
import operator
def solve():
    L = 4; M = 5
    MP = [list(map(int, input().split())) for i in range(L)]
    memo = {(0,)*(L**2): 0}
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    INF = 10
    def dfs(k, R):
        key = reduce(operator.add, map(tuple, R))
        if key in memo:
            return memo[key]
        if k == 0:
            return INF
        r = INF
        for i in range(L):
            for j in range(L):
                v = R[i][j]
                R0 = [e[:] for e in R]
                if R0[i][j] < 4:
                    R0[i][j] += 1
                    r = min(r, dfs(k-1, R0) + 1)
                    continue
                R0[i][j] = 0
                S = [(j, i, a) for a in range(4)]
                cnt = 1
                while S:
                    T = []
                    for x, y, d in S:
                        dx, dy = dd[d]
                        nx = x + dx; ny = y + dy
                        if not 0 <= nx < L or not 0 <= ny < L:
                            continue
                        if R0[ny][nx]:
                            R0[ny][nx] += 1
                        else:
                            T.append((nx, ny, d))
                    for y in range(L):
                        for x in range(L):
                            if R0[y][x] >= 5:
                                R0[y][x] = 0
                                cnt += 1
                                T.extend((x, y, a) for a in range(4))
                    S = T
                r = min(r, dfs(k-1, R0) + 1)
        memo[key] = r
        return r
    res = dfs(5, MP)
    print(res if res < INF else -1)
solve()
