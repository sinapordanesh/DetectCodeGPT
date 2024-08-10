import sys
def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    def gcd(m, n):
        while n:
            m, n = n, m % n
        return m

    def init(p, q=1):
        g = gcd(p, q)
        return p//g, q//g
    def add(A, B):
        pa, qa = A
        pb, qb = B
        if pa == 0:
            return B
        if pb == 0:
            return A
        g = gcd(qa, qb)
        ra = pa*qb//g + pb*qa//g; rb = qa*qb//g
        g = gcd(ra, rb)
        return ra // g, rb // g

    INF = 10**18
    def cp(X):
        vw, pf, vf, th = X
        if vw == 0:
            return INF
        return th/vw
    while 1:
        N = int(readline())
        if N == 0:
            break
        pw = int(readline())
        P = [list(map(int, readline().split())) for i in range(N)]
        P.append((1, 0, 1, 0))
        P.sort(key=cp)
        A = [init(0)]*(N+1)
        B = [init(0)]*(N+1)
        a = b = init(0)
        a = init(pw)
        for i, (vw, pf, vf, th) in enumerate(P):
            if vw == 0:
                if th > 0:
                    b = add(b, (th*pf, vf))
                continue
            if vw > 0:
                if th^vw >= 0:
                    a = add(a, (-vw*pf, vf))
                    b = add(b, (th*pf, vf))
                    A[i] = init(vw*pf, vf)
                    B[i] = init(-th*pf, vf)
            else:
                if th^vw >= 0:
                    A[i] = init(-vw*pf, vf)
                    B[i] = init(th*pf, vf)
                else:
                    a = add(a, (-vw*pf, vf))
                    b = add(b, (th*pf, vf))
        ans = INF
        for i, (vw, pf, vf, th) in enumerate(P):
            if vw == 0:
                continue
            if th^vw < 0:
                continue
            a = add(a, A[i]); b = add(b, B[i])
            pa, qa = a; pb, qb = b
            v = (pa*th*qb + pb*vw*qa) / (vw * qa * qb)
            if ans + 0.01 < v:
                break
            ans = min(ans, v)
        write("%.016f\n" % ans)
main()
