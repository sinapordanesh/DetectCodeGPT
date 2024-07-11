from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    RG0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
            RG0[lbt].add(lbs)
        GP[lbs].append(v)
    return G0, RG0, GP

def solve():
    N, M, T = map(int, readline().split())
    if N == M == T == 0:
        return False
    V = [0]*N; W = [0]*N; C = [0]*N
    for i in range(N):
        V[i], W[i], C[i] = map(int, readline().split())
    G = [[] for i in range(N)]
    RG = [[] for i in range(N)]
    SL = [0]*N
    for i in range(M):
        a, b = map(int, readline().split())
        if a == b:
            SL[a-1] = 1
        else:
            G[a-1].append(b-1)
            RG[b-1].append(a-1)
    label, group = scc(N, G, RG)
    G0, RG0, GP = construct(N, G, label, group)

    INF = 10**18
    dp = [None]*label
    zeros = [0] + [-INF]*T

    que = deque()
    deg = [0]*label
    for i in range(label):
        if len(RG0[i]) == 0:
            que.append(i)
            dp[i] = zeros[:]
        deg[i] = len(RG0[i])

    ans = 0
    dp1 = [0]*(T+1)
    while que:
        v = que.popleft()
        dp0 = dp[v]
        if len(GP[v]) == 1 and not SL[GP[v][0]]:
            e, = GP[v]
            ve = V[e]; we = W[e]
            for i in range(T, we-1, -1):
                dp0[i] = max(dp0[i], dp0[i-we] + ve)
        else:
            deq = deque()
            push = deq.append
            popl = deq.popleft
            pop = deq.pop
            clear = deq.clear
            for e in GP[v]:
                ve = V[e]; we = W[e]; ce = C[e]
                if T < we:
                    continue
                if ce == 1:
                    for i in range(T, we-1, -1):
                        dp0[i] = max(dp0[i], dp0[i-we] + ve)
                elif T <= we*ce:
                    for i in range(we, T+1):
                        dp0[i] = max(dp0[i], dp0[i-we] + ve)
                else:
                    for k in range(we):
                        for i in range((T - k) // we + 1):
                            v0 = dp0[k] - i*ve
                            while deq and deq[-1][1] <= v0:
                                pop()
                            push((i, v0))

                            dp0[k] = deq[0][1] + i*ve

                            if deq[0][0] == i-ce:
                                popl()
                            k += we
                        clear()
        ans = max(ans, max(dp0))

        for w in G0[v]:
            deg[w] -= 1
            if deg[w] == 0:
                que.append(w)
            if dp[w] is None:
                dp[w] = dp0[:]
            else:
                dp[w][:] = (max(p, q) for p, q in zip(dp[w], dp0))
    write("%d\n" % ans)
    return True
while solve():
    ...
