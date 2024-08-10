def main():
    while 1:
        N = int(input())
        if N == 0:
            break
        D = {}
        G = [set() for i in range(N)]
        cur = 0
        K = []
        PS = []
        for i in range(N):
            ps = []
            s = input()
            if s in D:
                k = D[s]
            else:
                D[s] = k = cur
                cur += 1
            while 1:
                d = input()
                if d == "-1":
                    break
                ps.append(list(map(int, d.split())))

            for j in range(i):
                if k == K[j]:
                    continue
                qs = PS[j]
                ok = 0
                for k1 in range(len(ps)):
                    x0, y0 = ps[k1-1]
                    x1, y1 = ps[k1]
                    dx = x1 - x0; dy = y1 - y0
                    for k2 in range(len(qs)):
                        X0, Y0 = qs[k2-1]
                        X1, Y1 = qs[k2]
                        if (X0 - x0)*dy == (Y0 - y0)*dx and (X1 - x0)*dy == (Y1 - y0)*dx:
                            if dx != 0:
                                s0 = (X0 - x0); s1 = (X1 - x0)
                                t = dx
                            else:
                                s0 = (Y0 - y0); s1 = (Y1 - y0)
                                t = dy
                            if t < 0:
                                s0 = -s0; s1 = -s1
                                t = -t
                            if not s0 < s1:
                                s0, s1 = s1, s0
                            if s0 < t and 0 < s1:
                                break
                    else:
                        continue
                    break
                else:
                    continue
                l = K[j]
                if k < l:
                    G[l].add(k)
                else:
                    G[k].add(l)
            K.append(k)
            PS.append(ps)
        def dfs(i, cs, ma):
            if i == cur:
                return max(cs)+1
            U = 0
            for j in G[i]:
                U |= 1 << cs[j]
            r = cur
            for k in range(ma+1):
                if U & 1 == 0:
                    cs[i] = k
                    r = min(r, dfs(i+1, cs, ma))
                U >>= 1
            cs[i] = ma+1
            r = min(r, dfs(i+1, cs, ma+1))
            return r
        print(dfs(0, [0]*cur, 0))
main()

