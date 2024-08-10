N, X, D = map(int, input().split())
M = [0]*N
M[0] = int(input())
P = [0]*N
for i in range(N-1):
    M[i+1], P[i+1] = map(int, input().split())

C = [1]*N
for i in range(N-1, 0, -1):
    p = P[i]-1
    C[p] += C[i]
    M[p] += M[i]
L = [D]*N
L[0] = X

from collections import deque

def solve(N, W, ws, vs, ms):
    V0 = max(vs)
    V = sum(v * min(V0, m) for v, m in zip(vs, ms))

    dp = [W+1]*(V + 1)
    dp[0] = 0
    for i in range(N):
        v = vs[i]; w = ws[i]; m = ms[i]
        c = min(V0, m)
        ms[i] -= c
        for k in range(v):
            que = deque()
            push = que.append
            popf = que.popleft; popb = que.pop

            for j in range((V-k)//v+1):
                a = dp[k + j*v] - j * w
                while que and a <= que[-1][1]:
                    popb()
                push((j, a))

                p, b = que[0]

                dp[k + j*v] = b + j * w
                if que and p <= j-c:
                    popf()

    *I, = range(N)
    I.sort(key=lambda x: ws[x]/vs[x])
    *S, = [(vs[i], ws[i], ms[i]) for i in I]

    def greedy():
        yield 0
        for i in range(V + 1):
            if dp[i] > W:
                continue
            rest = W - dp[i]
            r = i
            for v, w, m in S:
                m = min(m, rest // w)
                r += m * v
                rest -= m * w
            yield r
    return max(greedy())

print(solve(N, X, M, C, L))