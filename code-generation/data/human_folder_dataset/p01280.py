import sys
readline = sys.stdin.readline
write = sys.stdout.write

def gcd(m, n):
    while n:
        m, n = n, m % n
    return m
def lcm(m, n):
    return m // gcd(m, n) * n
def solve():
    N = int(readline())
    if N == 0:
        return False

    pp = [13, 17, 19, 23]
    E = [[0]*i for i in range(25)]
    Q = []
    for i in range(N):
        d, t, *qs = map(int, readline().split())
        qs = qs[t:] + qs[:t]
        Ed = E[d]
        for i in range(d):
            Ed[i] += qs[i]
    L = 13860
    V = [0]*L
    for i in range(1, 25):
        if i in pp:
            continue
        if i <= 12:
            Ei = E[i]; Ej = E[2*i]
            for j in range(2*i):
                Ej[j] += Ei[j % i]
        else:
            Ei = E[i]
            if i == 16:
                for j in range(8):
                    Ei[j] = max(Ei[j+8], Ei[j])
                Ej = E[24]
                for j in range(24):
                    Ej[j] += Ei[j % 8]
            elif i == 24:
                for j in range(12):
                    Ei[j] = max(Ei[j+12], Ei[j])
                for j in range(L):
                    V[j] += Ei[j % 12]
            else:
                for j in range(L):
                    V[j] += Ei[j % i]
    ans = max(V)
    for i in pp:
        ans += max(E[i])
    write("%d\n" % ans)
    return True
while solve():
    ...
