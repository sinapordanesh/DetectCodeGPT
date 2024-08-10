# seishin.py
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def gen(N, K):
    if K == 0:
        yield 0
        return
    v = (1 << K) - 1
    N2 = (1 << N)
    while v < N2:
        yield v
        x = v & -v; y = v + x
        v = ((v & ~y) // x >> 1) | y

def solve():
    R, C = map(int, readline().split())
    S = [readline().strip() for i in range(R)]
    C2 = (1 << C)
    bc = [0]*C2
    for state in range(1, C2):
        bc[state] = bc[state ^ (state & -state)] + 1

    LI = [None]*(C+1)
    RI = [None]*(C+1)
    for sl in range(C+1):
        r0 = [None]*(C+1)
        r1 = [None]*(C+1)
        for j in range(C+1):
            sr = sl - (C-j)
            e0 = []
            for k in range(max(sr, 0), min(sl, C)+1):
                e0.extend(gen(j, k))
            r0[j] = e0
            r1[j] = [state << (C-j) for state in e0]
        LI[sl] = r0
        RI[sl] = r1

    dp0 = [0]*C2; dp1 = [0]*C2
    zeros = [0]*C2
    s = S[0]; sl = len(s)
    for j in range(1, C):
        dp1[:] = zeros
        b0 = (1 << (j-1))
        b1 = (1 << j)
        for state in LI[sl][j]:
            ll = bc[state]
            dp1[state] = dp0[state]
            if ll < sl:
                if state & b0 and s[ll-1] == s[ll]:
                    dp1[state | b1] = dp0[state] + 2
                else:
                    dp1[state | b1] = dp0[state]
        dp0, dp1 = dp1, dp0
    for i in range(1, R):
        p = S[i-1]; pl = len(p)
        s = S[i]; sl = len(s)
        for j in range(C):
            dp1[:] = zeros
            b0 = (1 << (j-1)) if j else 0
            b1 = (1 << j)
            L0 = LI[sl][j]; R0 = RI[pl][C-j-1]
            for state1 in L0:
                ll = bc[state1]
                if ll < sl:
                    c = s[ll]
                    for state2 in R0:
                        rl = bc[state2]
                        state = state1 | state2
                        n_state = state | b1

                        if j < C-1:
                            dp1[state] = max(dp0[state], dp0[n_state]) if rl < pl else dp0[state]
                        r1 = max(dp0[state], (dp0[n_state] + 2 if (p[-rl-1] == c) else dp0[n_state])) if rl < pl else dp0[state]
                        if state & b0 and s[ll-1] == c:
                            dp1[n_state] = r1 + 2
                        else:
                            dp1[n_state] = r1
                else:
                    for state2 in R0:
                        state = state1 | state2
                        if bc[state2] < pl:
                            dp1[state] = max(dp0[state], dp0[state | b1])
                        else:
                            dp1[state] = dp0[state]
            dp0, dp1 = dp1, dp0
    write("%d\n" % max(dp0))
solve()
