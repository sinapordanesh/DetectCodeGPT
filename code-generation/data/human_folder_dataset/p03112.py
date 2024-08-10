import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def neighborhood(L, now):
    tmp = bisect_left(L, now)
    if tmp == 0:
        return [tmp, None]
    elif tmp == len(L):
        return [tmp - 1, None]
    else:
        return [tmp - 1, tmp]


def dist_calc(now, p1, p2):
    if p1 is None or p2 is None:
        return f_inf
    res1 = abs(now - p1) + abs(p1 - p2)
    res2 = abs(now - p2) + abs(p1 - p2)
    return min(res1, res2)


def resolve():
    a, b, q = map(int, input().split())
    S = list(int(input()) for _ in range(a))
    T = list(int(input()) for _ in range(b))
    query = list(int(input()) for _ in range(q))

    for x in query:
        dist1 = f_inf
        s1, s2 = neighborhood(S, x)
        for s in [s1, s2]:
            if s is not None:
                t1, t2 = neighborhood(T, S[s])
                for t in [t1, t2]:
                    if t is not None:
                        dist1 = min(dist1, dist_calc(x, S[s], T[t]))

        dist2 = f_inf
        t1, t2 = neighborhood(T, x)
        for t in [t1, t2]:
            if t is not None:
                s1, s2 = neighborhood(S, T[t])
                for s in [s1, s2]:
                    if s is not None:
                        dist2 = min(dist2, dist_calc(x, S[s], T[t]))

        res = min(dist1, dist2)
        print(res)


if __name__ == '__main__':
    resolve()
