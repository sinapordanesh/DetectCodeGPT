def solve():
    from math import acos
    from cmath import phase, rect, pi
    
    from sys import stdin
    file_input = stdin
    
    while True:
        n = int(file_input.readline())
        if n == 0:
            break
        
        C = (map(int, file_input.readline().split()) for i in range(n))
        P = []
        x, y, r1 = next(C)
        c1 = x + y * 1j
        P.append(c1)
        
        # calculation of cross points of circles
        for x, y, r2 in C:
            c2 = x + y * 1j
            
            base = c2 - c1
            d = abs(base)
            a = acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
            t = phase(base)
            cp1 = c1 + rect(r1, t + a)
            cp2 = c1 + rect(r1, t - a)
            
            P.append(cp1)
            P.append(cp2)
            
            c1, r1 = c2, r2
        
        # search path and calculation of its cost
        lim = 5000
        dist = [lim] * (2 * n)
        dist[0] = 0
        goal = c1
        g_idx = 2 * n - 1
        indices = ((i + (i % 2) + 1, i + (i % 2) + 2) for i in range(g_idx))
        
        for tpl_idx, cp, d in zip(indices, P, dist):
            j, k = tpl_idx
            s1 = None
            s2 = None
            p_s1 = None
            p_s2 = None
            for l, cp1, cp2 in zip(range(j, g_idx, 2), P[j::2], P[k::2]):
                t_s1 = cp1 - cp
                t_s2 = cp2 - cp
                if s1 is None or phase(s1 / t_s1) >= 0:
                    s1 = t_s1
                if s2 is None or phase(s2 / t_s2) <= 0:
                    s2 = t_s2
                if phase(s1 / s2) < 0:
                    break
                
                if p_s1 != s1:
                    dist[l] = min(dist[l], d + abs(s1))
                    p_s1 = s1
                if p_s2 != s2:
                    dist[l+1] = min(dist[l+1], d + abs(s2))
                    p_s2 = s2
            else:
                gs = goal - cp
                if (s1 is None and s2 is None) or \
                phase(s1 / gs) >= 0 and phase(s2 / gs) <= 0:
                    dist[g_idx] = min(dist[g_idx], d + abs(gs))
        
        print(dist[g_idx])

solve()
