from string import digits
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, L = map(int, readline().split())
    S = readline().strip()
    *I, = range(N*N)
    LRUD = "LRUD"
    FS = [[], [], [], []]
    for i in range(N):
        base = N*i
        F = I[:]
        for j in range(N):
            F[base+j] = base+((j+1) % N)
        FS[0].append(F)
        F = I[:]
        for j in range(N):
            F[base+j] = base+((j-1) % N)
        FS[1].append(F)

        base = i
        F = I[:]
        for j in range(N):
            F[base+N*j] = base+((j+1) % N)*N
        FS[2].append(F)
        F = I[:]
        for j in range(N):
            F[base+N*j] = base+((j-1) % N)*N
        FS[3].append(F)

    def fast_pow(f, n):
        r = I[:]
        while n:
            if n & 1:
                r = [f[x] for x in r]
            f = [f[x] for x in f]
            n >>= 1
        return r

    S += "$"
    cur = 0
    def number():
        nonlocal cur
        r = 0
        while S[cur] in digits:
            r = 10*r + int(S[cur])
            cur += 1 # digits
        return r

    def expr():
        nonlocal cur
        f0 = I[:]
        while 1:
            if S[cur] == '(':
                cur += 1 # '('
                r1 = expr()
                cur += 1 # ')'
                num = number()
                f1 = fast_pow(r1, num)
            elif S[cur] in LRUD:
                t = LRUD.index(S[cur])
                cur += 1 # LRUD
                num = number()
                f1 = FS[t][num-1]
            else:
                break
            f0 = [f0[x] for x in f1]
        return f0

    f = expr()
    ans = [str(x+1) for x in f]
    for i in range(N):
        write(" ".join(ans[i*N:i*N+N]))
        write("\n")
solve()
