from heapq import heappush, heappop, heapify

import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    P = []; Q = []
    E = []; R = {}
    L = N + 20000
    for i in range(N):
        s, a = readline().split(); a = int(a) * L + i
        E.append(s)
        Q.append((-a, i))
        R[s] = (i, a)
    heapify(Q)
    for i in range(N // 5):
        b, i = heappop(Q)
        P.append((-b, i))
    heapify(P)

    pn = len(P); qn = len(Q)
    ln = N

    cur = N
    M = int(readline())
    for i in range(M):
        p, *g = readline().split()
        db = dk = -1
        if p == "+":
            t, b = g; b = int(b) * L + cur
            E.append(t)
            R[t] = (cur, b)
            ln += 1
            if ln >= 5 and -Q[0][0] < b:
                da = 1
                pn += 1
                heappush(P, (b, cur))
                if pn > ln // 5:
                    while 1:
                        c, k = heappop(P)
                        if E[k] is not None:
                            if c == b:
                                da = 0
                            else:
                                db = 0
                                dk = k
                            heappush(Q, (-c, k))
                            break
                    pn -= 1; qn += 1
            else:
                da = 0
                qn += 1
                heappush(Q, (-b, cur))
                if pn < ln // 5:
                    while 1:
                        c, k = heappop(Q)
                        if E[k] is not None:
                            if -b == c:
                                da = 1
                            else:
                                db = 1
                                dk = k
                            heappush(P, (-c, k))
                            break
                    pn += 1; qn -= 1
            if da:
                write("%s is working hard now.\n" % t)
            else:
                write("%s is not working now.\n" % t)
            cur += 1
        else:
            t, = g
            j, b = R[t]
            E[j] = None
            ln -= 1
            if P and P[0][0] <= b:
                pn -= 1
                if pn < ln // 5:
                    while 1:
                        c, k = heappop(Q)
                        if E[k] is not None:
                            heappush(P, (-c, k))
                            db = 1; dk = k
                            break
                    pn += 1; qn -= 1
            else:
                qn -= 1
                if pn > ln // 5:
                    while 1:
                        c, k = heappop(P)
                        if E[k] is not None:
                            heappush(Q, (-c, k))
                            db = 0; dk = k
                            break
                    qn += 1; pn -= 1
        if db != -1:
            if db:
                write("%s is working hard now.\n" % E[dk])
            else:
                write("%s is not working now.\n" % E[dk])
solve()

