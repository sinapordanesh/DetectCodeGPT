from functools import cmp_to_key

def f(a, b):
    if a[0] == b[0]:
        ap = a[1] + a[2] * 20
        bp = b[1] + b[2] * 20
        if ap == bp:
            return a[3] > b[3]
        return ap < bp
    return a[0] > b[0]


while True:
    M, T, P, R = map(int, input().split())
    if not M:
        break
    fail = [[0 for i in range(P)] for j in range(T)]
    # [-solved, time, -team]
    res = [[0, 0, -i] for i in range(T)]
    
    for r in range(R):
        m, t, p, j = map(int, input().split())
        t -= 1
        p -= 1
        if j:
            fail[t][p] += 1
        else:
            res[t][0] -= 1
            res[t][1] += fail[t][p] * 20 + m
    res = sorted(res)
    for i, r in enumerate(res[:-1]):
        if r[0] == res[i + 1][0] and r[1] == res[i + 1][1]:
            print(-r[2] + 1, end='=')
        else:
            print(-r[2] + 1, end=',')
    print(-res[-1][2] + 1)