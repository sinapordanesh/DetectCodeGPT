N, M, Q = map(int, input().split())
res = 0

def dfs(L: list):
    global res
    A = L[::]
    if len(A) == N + 1:
        now = 0
        for i in range(Q):
            if A[b[i]] - A[a[i]] == c[i]:
                now += d[i]
        res = max(res, now)
        # print(A, now)
        return
    
    A.append(A[-1])
    while A[-1] <= M:
        dfs(A)
        A[-1] += 1
    
a, b, c, d = [], [], [], []
for _ in range(Q):
    _a, _b, _c, _d = map(int, input().split())
    a.append(_a)
    b.append(_b)
    c.append(_c)
    d.append(_d)

dfs([1])
print(res)
