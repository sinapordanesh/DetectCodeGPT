import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    L = [0]*N; D = [0]*N
    for i in range(N):
        l, d = readline().split()
        L[i] = +(l == 'y')
        D[i] = int(d)
    ans = 0
    *I, = range(N)
    I.sort(key = D.__getitem__)
    U = [0]*N
    for i in I:
        if not L[i] or U[i]:
            continue
        d = D[i]
        U[i] = 1
        ans += 1
        k = i-1
        while k >= 0 and (L[k] or D[k] < d):
            if L[k]:
                U[k] = 1
            k -= 1
        k = i+1
        while k < N and (L[k] or D[k] < d):
            if L[k]:
                U[k] = 1
            k += 1
    write("%d\n" % ans)
solve()
