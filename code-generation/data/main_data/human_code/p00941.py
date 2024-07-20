from heapq import heappush, heappop

def solve():
    S = input()
    K = int(input())
    L = len(S)
    INF = 10**9
    cost = [[INF]*(L+1) for i in range(L+1)]
    cost[0][L] = 0
    ss = []
    que = [(0, 0, L)]
    while que:
        d, a, b = heappop(que)
        if cost[a][b] < d:
            continue
        ss.append((a, b))
        if a+1 == b:
            if d+1 < cost[a+1][b]:
                cost[a+1][b] = d + 1
            continue
        if S[a] == S[b-1]:
            if d+2 < cost[a+1][b-1]:
                cost[a+1][b-1] = d + 2
                if a+1 < b-1:
                    heappush(que, (d+2, a+1, b-1))
        else:
            if d+2 < cost[a+1][b]:
                cost[a+1][b] = d + 2
                if a+1 < b:
                    heappush(que, (d+2, a+1, b))
            if d+2 < cost[a][b-1]:
                cost[a][b-1] = d + 2
                if a < b-1:
                    heappush(que, (d+2, a, b-1))
    ln = min(cost[i][i] for i in range(L+1))
    ss.reverse()
    dp = [[0]*(L+1) for i in range(L+1)]
    for i in range(L+1):
        if cost[i][i] == ln:
            dp[i][i] = 1
    for a, b in ss:
        d = cost[a][b]
        r = 0
        if a+1 == b:
            if d+1 == cost[a+1][b]:
                r = dp[a+1][b]
        else:
            if S[a] == S[b-1]:
                if d+2 == cost[a+1][b-1]:
                    r = dp[a+1][b-1]
            else:
                if d+2 == cost[a+1][b]:
                    r += dp[a+1][b]
                if d+2 == cost[a][b-1]:
                    r += dp[a][b-1]
        dp[a][b] = r
    if dp[a][b] < K:
        print("NONE")
        return True
    SL = []; SR = []
    a = 0; b = L
    while a < b:
        if a+1 == b:
            assert cost[a][b]+1 == cost[a+1][b]
            SL.append(S[a])
            a += 1
            continue
        if S[a] == S[b-1]:
            assert cost[a][b]+2 == cost[a+1][b-1]
            SL.append(S[a])
            SR.append(S[b-1])
            a += 1; b -= 1
        elif S[a] < S[b-1]:
            c = (cost[a][b]+2 == cost[a+1][b])
            if c and K <= dp[a+1][b]:
                SL.append(S[a])
                SR.append(S[a])
                a += 1
            else:
                if c:
                    K -= dp[a+1][b]
                SL.append(S[b-1])
                SR.append(S[b-1])
                b -= 1
        else:
            c = (cost[a][b]+2 == cost[a][b-1])
            if c and K <= dp[a][b-1]:
                SL.append(S[b-1])
                SR.append(S[b-1])
                b -= 1
            else:
                if c:
                    K -= dp[a][b-1]
                SL.append(S[a])
                SR.append(S[a])
                a += 1
    SR.reverse()
    SL.extend(SR)
    print("".join(SL))
solve()
