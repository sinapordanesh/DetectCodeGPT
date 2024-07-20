import sys
readline = sys.stdin.readline
write = sys.stdout.write
sys.setrecursionlimit(10**5)
def solve():
    N = int(readline())
    if N == 0:
        return False
    S = readline().strip() + "$"
    L = len(S)
    pt = [0]*L
    st = []
    for i in range(L):
        if S[i] == '(':
            st.append(i)
        elif S[i] == ')':
            k = st.pop()
            pt[i] = k
            pt[k] = i

    ans = 0
    def parse(cur):
        nonlocal ans
        ps = []
        ls = []
        su = 0
        while 1:
            ms = []
            while 1:
                if S[cur] == '(':
                    v = parse(cur+1)
                    cur = pt[cur]+1
                else:
                    v = int(S[cur])
                    cur += 1
                ms.append(v)
                if S[cur] != '*':
                    break
                cur += 1
            l = len(ms)
            ms_a = [1]*(l+1)
            for i in range(l):
                ms_a[i+1] = ms_a[i] * ms[i]
            ps.append(ms_a)
            ls.append(l)
            su += ms_a[-1]
            if S[cur] != '+':
                break
            cur += 1
        p1 = c1 = 0; s1 = 0
        q1 = d1 = 0; t1 = 0; u1 = 0
        q2 = d2 = 0; t2 = 0; u2 = 0
        s = 0
        while p1 < len(ls):
            k1 = ps[p1][c1+1]
            if s1 + k1 >= N:
                break
            if c1 + 1 < ls[p1]:
                c1 += 1
            else:
                s1 += ps[p1][-1]
                p1 += 1; c1 = 0
        while p1 < len(ls):
            k1 = ps[p1][c1+1]
            while (q1, d1) <= (p1, c1):
                k2 = ps[q1][d1]
                if p1 == q1:
                    v = (s1 - t1) + (k1 // k2)
                else:
                    kk = ps[q1][-1]
                    v = (s1 - t1) + (k1 + kk // k2 - kk)
                if v >= N:
                    if d1 + 1 < ls[q1]:
                        d1 += 1
                    else:
                        t1 += ps[q1][-1]
                        q1 += 1; d1 = 0
                    u1 += 1
                else:
                    break
            while (q2, d2) <= (p1, c1):
                k3 = ps[q2][d2]
                if p1 == q2:
                    v = (s1 - t2) + (k1 // k3)
                else:
                    kk = ps[q2][-1]
                    v = (s1 - t2) + (k1 + kk // k3 - kk)
                if v > N:
                    if d2 + 1 < ls[q2]:
                        d2 += 1
                    else:
                        t2 += ps[q2][-1]
                        q2 += 1; d2 = 0
                    u2 += 1
                else:
                    break
            ans += u1 - u2
            if c1 + 1 < ls[p1]:
                c1 += 1
            else:
                s1 += ps[p1][-1]
                p1 += 1; c1 = 0
        return su
    parse(0)
    write("%d\n" % ans)
    return True
while solve():
    ...
