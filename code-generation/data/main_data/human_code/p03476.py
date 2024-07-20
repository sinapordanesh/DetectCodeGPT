import bisect
Q = int(input())
lsQ = []
for i in range(Q):
    l,r = map(int,input().split())
    lsQ.append([l,r])
def prime(N):
    lsprime = [0,0]+[1 for i in range(N-1)]
    lsprime2 = []
    for i in range(N+1):
        if lsprime[i] == 0:
            continue
        lsprime2.append(i)
        k = i
        while i <= N:
            lsprime[i] = 0
            i += k
    return lsprime2

primels = prime(10**5)
primeset = set(primels)
lssim = []
for i in primels:
    x = (i+1)//2
    if x in primeset:
        lssim.append(i)
for i in range(Q):
    ans = bisect.bisect(lssim,lsQ[i][1])-bisect.bisect_left(lssim,lsQ[i][0])
    print(ans)