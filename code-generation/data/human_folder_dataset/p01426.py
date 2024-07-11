import sys
readline = sys.stdin.readline
write = sys.stdout.write

def calc(V, es, r):
    mins = [(10**18, -1)]*V
    for s, t, w in es:
        mins[t] = min(mins[t], (w, s))
    mins[r] = (-1, -1)

    group = [0]*V
    comp = [0]*V
    cnt = 0

    used = [0]*V
    for v in range(V):
        if not used[v]:
            chain = []
            cur = v
            while cur!=-1 and not used[cur]:
                chain.append(cur)
                used[cur] = 1
                cur = mins[cur][1]
            if cur!=-1:
                cycle = 0
                for e in chain:
                    group[e] = cnt
                    if e==cur:
                        cycle = 1
                        comp[cnt] = 1
                    if not cycle:
                        cnt += 1
                if cycle:
                    cnt += 1
            else:
                for e in chain:
                    group[e] = cnt
                    cnt += 1

    if cnt == V:
        return sum(map(lambda x:x[0], mins)) + 1

    res = sum(mins[v][0] for v in range(V) if v!=r and comp[group[v]])

    n_es = []
    for s, t, w in es:
        gs = group[s]; gt = group[t]
        if gs == gt:
            continue
        if comp[gt]:
            n_es.append((gs, gt, w - mins[t][0]))
        else:
            n_es.append((gs, gt, w))
    return res + calc(cnt, n_es, group[r])

def solve():
    N, M = map(int, readline().split())
    V = []
    D = []
    for i in range(M):
        *Vi, = map(float, readline().split())
        d = sum(e**2 for e in Vi)
        if d <= 1e-9:
            continue
        V.append(Vi)
        D.append(d)

    M = len(V)
    E = []
    for i in range(M):
        Vi = V[i]
        for j in range(M):
            if i == j:
                continue
            Vj = V[j]
            t = 0
            for k in range(N):
                t += Vi[k] * Vj[k]
            r = t / (D[j])
            c = 0
            for k in range(N):
                c += (Vi[k] - r*Vj[k])**2
            E.append((j+1, i+1, c))
        E.append((0, i+1, D[i]))
    write("%.16f\n" % calc(M+1, E, 0))
solve()
