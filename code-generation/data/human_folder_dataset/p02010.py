from heapq import heappush, heappop, heapify
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    S = readline().strip()
    L = len(S)
    S += "+"
    if L % 2 == 0 and N < 10:
        write("-1\n")
        return
    pw10 = [1]*11
    for i in range(10):
        pw10[i+1] = pw10[i] * 10
    INF = N+1
    dist = [[INF]*(L+2) for i in range(L+1)]
    ques = [[] for i in range(L+1)]
    ques[0] = [(0, 0)]
    dist[0][0] = 0
    for k in range(L+1):
        que = ques[k]
        dist0 = dist[k]
        heapify(que)
        while que:
            cost, i = heappop(que)
            if dist0[i] < cost or i > L:
                continue

            p = S[i]
            if i+1 != L-1:
                if p != "+":
                    v = int(p)
                    if S[i+1] != '+':
                        if cost + v < dist[k+1][i+2]:
                            dist[k+1][i+2] = cost + v
                            ques[k+1].append((cost + v, i+2))
                    else:
                        if cost + v < dist0[i+2]:
                            dist0[i+2] = cost + v
                            heappush(que, (cost + v, i+2))
                if p != "0":
                    nk = k+1 + (S[i+1] != "+")
                    if cost < dist[nk][i+2]:
                        dist[nk][i+2] = cost
                        ques[nk].append((cost, i+2))
            def calc(c0, p):
                for j in range(i+2, min(i+10, L+1)):
                    if j == L-1:
                        continue
                    p1 = p + S[i+1:j]; l = j-i
                    c = c0 + p1.count("+")
                    v = int(p1.replace(*"+0"))
                    if v <= N:
                        nk = k+c + (S[j] != '+')
                        if cost + v < dist[nk][j+1]:
                            dist[nk][j+1] = cost + v
                            ques[nk].append((cost + v, j+1))
                    b = pw10[l-2]
                    for e in range(l-2, -1, -1):
                        a = (v // b) % 10
                        if a:
                            v -= a * b
                            c += 1
                            if v <= N:
                                nk = k+c + (S[j] != '+')
                                if cost + v < dist[nk][j+1]:
                                    dist[nk][j+1] = cost + v
                                    ques[nk].append((cost + v, j+1))
                        b //= 10
            if p not in "0+":
                calc(0, p)
            if p != "1":
                calc(1, "1")
        if dist0[L+1] <= N:
            write("%d\n" % k)
            break
solve()
