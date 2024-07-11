import sys
readline = sys.stdin.readline
write = sys.stdout.write

D = [
    (1, 5, 2, 3, 0, 4), # 'U'
    (3, 1, 0, 5, 4, 2), # 'R'
    (4, 0, 2, 3, 5, 1), # 'D'
    (2, 1, 5, 0, 4, 3), # 'L'
]
p_dice = (0, 0, 0, 1, 1, 2, 2, 3)*3

def enumerate_dice(L0):
    L = L0[:]
    for k in p_dice:
        yield L
        L[:] = (L[e] for e in D[k])

L = [1, 2, 3, 4, 5, 6]
LS = []
for l in enumerate_dice(L):
    LS.append(l[:])

def solve():
    T = [list(map(int, readline().split())) for i in range(3)]
    F = [list(map(int, readline().split())) for i in range(3)]

    T0 = [[-1]*3 for i in range(3)]
    F0 = [[-1]*3 for i in range(3)]
    R0 = [[-1]*3 for i in range(3)]
    res = set()
    def dfs(i, s):
        if i == 27:
            res.add(s)
            return
        x = i % 3; y = (i // 3) % 3; z = (i // 9) % 3
        t0 = T0[y][x]
        f0 = F0[z][x]
        r0 = R0[z][y]
        for l in LS:
            if t0 == -1:
                e = T[y][x]
                if e != 0 and e != l[0]:
                    continue
                T0[y][x] = l[0]
            else:
                if l[0] != t0:
                    continue
            if f0 == -1:
                e = F[z][x]
                if e != 0 and e != l[1]:
                    continue
                F0[z][x] = l[1]
            else:
                if l[1] != f0:
                    continue
            if r0 == -1:
                R0[z][y] = l[2]
                s0 = s + l[2]
            else:
                if l[2] != r0:
                    continue
                s0 = s
            dfs(i+1, s0)
        if t0 == -1:
            T0[y][x] = -1
        if f0 == -1:
            F0[z][x] = -1
        if r0 == -1:
            R0[z][y] = -1
    dfs(0, 0)
    if res:
        ans = sorted(res)
        write(" ".join(map(str, ans)))
        write("\n")
    else:
        write("0\n")

N = int(readline())
for i in range(N):
    solve()
