import numpy as np


def solve(n, m):
    def prepare(n, m):
        f = 1
        for i in range(1, n + 1):
            f = f * i % m
        fn = f
        inv = [1] * (n + 1)
        f = pow(f, m - 2, m)
        inv[n] = f
        for i in range(n, 0, -1):
            f = f * i % m
            inv[i - 1] = f
        return fn, inv

    def a_x(a, x, m):
        ret = 1
        yield ret
        for _ in range(x):
            ret = ret * a % m
            yield ret

    fn, inv = prepare(n, m)

    stir2 = np.zeros(n + 2, dtype=np.int64)
    stir2[0] = 1
    upd = np.arange(2, n + 3, dtype=np.int64)

    ex2 = [2]
    for i in range(n):
        ex2.append(ex2[-1] ** 2 % m)

    ans = 0
    si = 1

    for i in range(n+1):
        nCi = fn * inv[i] * inv[n-i] % m
        i_with = np.fromiter(a_x(pow(2, n-i, m), i, m), dtype=np.int64) 
        i_on = (stir2[ :i+1] * i_with % m).sum() % m
        ans = (ans + nCi * i_on % m * ex2[n-i] % m * si) % m
        stir2[1 : i+2] = (stir2[1 : i+2] * upd[ :i+1] + stir2[ :i+1]) % m
        si *= -1

    return ans


N, M = map(int, input().split())
print(solve(N, M))
