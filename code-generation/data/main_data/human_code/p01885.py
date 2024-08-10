import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, L = map(int, readline().split())
    P = [list(map(int, readline().split())) for i in range(N)]
    C = [int(readline()) for i in range(N)]

    P.sort(key = lambda x: (x[0] - x[1]), reverse=1)

    INF = 10**18

    S = [0]*(N+1)
    s = 0
    for i in range(N):
        a, b = P[i]
        S[i+1] = s = s + (a - b)

    min1 = [INF]*(N+1)
    S0 = [0]*(N+1)
    s = 0; cur = INF
    for i in range(N):
        a, b = P[i]
        s += (a - b) - C[i]
        S0[i+1] = s
        min1[i+1] = cur = min(cur, s)

    N0 = 2**N.bit_length()
    data = [INF]*(N0*2)
    s = 0
    S1 = [0]*(N+1)
    for i in range(1, N):
        a, b = P[i]
        s += (a - b) - C[i-1]
        S1[i+1] = data[N0+i] = s
    for i in range(N0-2, -1, -1):
        data[i] = min(data[2*i+1], data[2*i+2])

    def query(l, r):
        L = l + N0; R = r + N0
        s = INF
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, data[R-1])

            if L & 1:
                s = min(s, data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

    if max(a for a, b in P) >= L:
        write("1\n")
        return

    ans = N+1
    k = N

    m = 0
    for i in range(N-1, -1, -1):
        a, b = P[i]
        m = max(m, a)
        if S[i] + m >= L and min1[i] > 0:
            ans = i+1
            k = i+1

    for i in range(k):
        a, b = P[i]
        left = 0; right = N+1
        while left+1 < right:
            mid = (left + right) >> 1
            if (S[mid] if mid < i+1 else S[mid]-(a-b)) < L-a:
                left = mid
            else:
                right = mid
        r = left
        if r == N:
            continue
        if r < i:
            if min1[r+1] > 0:
                ans = min(ans, r+2)
        else:
            if min1[i] > 0 and query(i+2, r+2) - S1[i+1] + S0[i] > 0:
                ans = min(ans, r+1)

    if ans == N+1:
        write("-1\n")
    else:
        write("%d\n" % ans)
solve()
