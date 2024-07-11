from collections import defaultdict, deque
from itertools import product

def primes(N):
    sieve = [True] * (N+1)
    sieve[:1] = [False, False]
    for i in range(N):
        if sieve[i]:
            for j in range(2*i, N+1, i):
                sieve[j] = False
    return sieve

cave = defaultdict(int)
cave[(0, 0)] = 1
sieve = primes(10**6)
D = [[0, 1], [-1, 0], [0, -1], [1, 0]]
where = [[10**7, 10**7], [0, 0]]

c = 0 # cycle
d = 3 # direction
x, y = 0, 0
dx, dy = 1, 0
for i in range(2, 10**6+1):
    if abs(x+dx) > c or abs(y+dy) > c:
        if d == 3:
            x, y = x+dx, y+dy
            c += 1
            d = 0
            dx, dy = D[d]
        else:
            d += 1
            dx, dy = D[d]
            x, y = x+dx, y+dy
    else:
        x, y = x+dx, y+dy
    where.append([x, y])
    cave[(x, y)] = i

M, N = map(int, input().split())

while N:
    x, y = where[N]
    Q = deque([[x, y]])
    DP = [0] * (M+1)
    DP[N] += sieve[N]
    searched = [False] * (M+1)
    while Q:
        #print(x, y)
        x, y = Q.popleft()
        ny = y - 1
        p = DP[cave[(x, y)]]
        for nx in range(x-1, x+2):
            n = cave[(nx, ny)]
            if 1 <= n <= M:
                DP[n] = max(DP[n], p + sieve[n])
                if not searched[n]:
                    searched[n] = True
                    Q.append([nx, ny])
    A = max(DP)
    B = 0
    if A:
        for i in range(M+1):
            if sieve[i] and DP[i] == A:
                B = i
    print(A, B)

    M, N = map(int, input().split())
