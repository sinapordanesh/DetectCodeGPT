def solve():
    N = int(input())
    T0 = []
    T1 = []
    su = 0
    for i in range(N):
        s = input()
        a = 0
        for c in s:
            if c == '(':
                a += 1
            elif a > 0:
                a -= 1
        b = 0
        for c in reversed(s):
            if c == ')':
                b += 1
            elif b > 0:
                b -= 1
        if b < a:
            T0.append((b, a))
        else:
            T1.append((a, b))
        su += a - b
    if su != 0:
        print("No")
        return

    def check(T, N):
        U = [0]*N
        cur = 0
        for i in range(N):
            k = -1; e = (-1000, -1000)
            for j in range(N):
                if U[j]:
                    continue
                b, a = T[j]
                if b <= cur:
                    ne = (a-b, b)
                    if e < ne:
                        k = j
                        e = ne
            if k == -1:
                return 0
            b, a = T[k]
            U[k] = 1
            cur += a-b
        return 1

    if check(T0, len(T0)) and check(T1, len(T1)):
        print("Yes")
    else:
        print("No")
solve()
