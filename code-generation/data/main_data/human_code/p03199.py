import sys
from collections import Counter, defaultdict, deque
readline = sys.stdin.readline

MOD = 998244353
def calc():
    N, M = map(int, readline().split())
    D = Counter()
    Grid = defaultdict(lambda: -1)
    flag = True
    geta = N
    co = 0
    for _ in range(M):
        a, b, c = map(int, readline().split())
        a -= 1
        b -= 1
        
        if abs(b - a) >= 3:
            if a > b:
                a, b = b, a
            if (a, b) in D:
                if D[(a, b)] != c:
                    flag = False
            else:
                D[(a, b)] = c
                co += 1
        else:
            Grid[a*geta+b] = c
    
    if not flag:
        return 0
        
    for i in range(N-2):
        g = Grid[(i+1)*geta+(i+1)]
        g1 = Grid[i*geta+(i+2)]
        g2 = Grid[(i+2)*geta+i]
        if g1 == -1 or g2 == -1:
            continue
        if g != -1:
            if (g1 == g2) == g:
                return 0
        else:
            Grid[(i+1)*geta+(i+1)] = int(g1 != g2)
    

    
    Edge = [[] for _ in range(N)]
    for i in range(N-1):
        g1 = Grid[(i+1)*geta+i]
        g2 = Grid[i*geta+(i+1)]
        if g1 == -1 or g2 == -1:
            continue
        
        k = int(g1 != g2)
        Edge[i].append((i+1, k))
        Edge[i+1].append((i, k))
    
    Diag = [None]*N
    Q = []
    for i in range(N):
        if Grid[i*geta+i] != -1:
            Diag[i] = Grid[i*geta+i]
            Q.append(i)
    
    
    Q = deque(Q)
    while Q:
        vn = Q.pop()
        for vf, k in Edge[vn]:
            if Diag[vf] is None:
                Diag[vf] = k^Diag[vn]
                Q.appendleft(vf)
            else:
                if Diag[vf] != k^Diag[vn]:
                    return 0
    
    
    jj = set()
    for vn in range(N):
        for vf, k in Edge[vn]:
            if Diag[vn] is None:
                jj.add((min(vn, vf), max(vn, vf)))
    
    co += len(jj)
    co += N - Diag.count(None)
    used = set()
    
    for i in range(N-1):
        if Grid[i*geta + (i+1)] != -1:
            used.add((i, i+1))
        if Grid[(i+1)*geta + i] != -1:
            used.add((i, i+1))
    
    for i in range(N-2):
        if Grid[i*geta + (i+2)] != -1:
            used.add((i, i+2))
        if Grid[(i+2)*geta + i] != -1:
            used.add((i, i+2))
    
    co += len(used)
    return pow(2, N*(N+1)//2 - co, MOD)

print(calc())
                    
            
