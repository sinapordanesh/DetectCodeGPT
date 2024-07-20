def rec(r, b, c, a0, n, mod):
    # a_n = r * a_{n-1} + b * n + c
    a = a0
    n_ = 0
    c += b
    diff = 1
    while n:
        n, m = divmod(n, 2)
        if m:
            a = (a * r + b * n_ + c) % mod
            n_ += diff
        r, b, c = r*r%mod, (r*b+b)%mod, (r*c+b*diff+c)%mod
        diff <<= 1
    return a

def main():
    L, A, B, M = map(int, input().split())

    def bis(d):
        # d 桁以上になる最小の項
        n = 10**(d-1)
        ng = -1
        ok = L
        while ng + 1 < ok:
            c = ok+ng >> 1
            s_c = A + B * c
            if s_c >= n:
                ok = c
            else:
                ng = c
        return ok
    Idxs = [0]
    for d in range(1, 19):
        Idxs.append(bis(d))
    Idxs.append(L)

    ans = 0
    for d, (l, r) in enumerate(zip(Idxs, Idxs[1:])):
        if r - l == 0:
            continue
        s_l = A + B * l
        n = r - l
        ratio = 10**d
        a = rec(ratio, B, s_l, s_l, n-1, M)
        #print(d, a)
        ans = (ans * pow(10, d*n, M) + a) % M
    print(ans)

main()
