mod = 10 ** 6 + 3


class Combi():
    def __init__(self, N, mod):
        self.power = [1 for _ in range(N+1)]
        self.rev = [1 for _ in range(N+1)]
        self.mod = mod
        for i in range(2, N+1):
            self.power[i] = (self.power[i-1]*i) % self.mod
        self.rev[N] = pow(self.power[N], self.mod-2, self.mod)
        for j in range(N, 0, -1):
            self.rev[j-1] = (self.rev[j]*j) % self.mod

    def com(self, K, R):
        if K < R:
            return 0
        else:
            return ((self.power[K])*(self.rev[K-R])*(self.rev[R])) % self.mod

    def pom(self, K, R):
        if K < R:
            return 0
        else:
            return (self.power[K])*(self.rev[K-R]) % self.mod

    def powe(self, K):
        return self.power[K]

    def rev_powe(self, K):
        return self.rev[K]


combi = Combi(mod-1, mod)


def rev(X):
    return pow(X, mod-2, mod)


def count_div(L, R, D):
    return not bool(R//D - (L-1)//D)


def solve():
    x, d, n = map(int, input().split())
    if d % (mod) == 0:
        print(pow(x,n,mod))
        return
    elif d % (mod) != 0:
        y = rev(d)*x
        if count_div(y, y+n-1, mod):
            y = y % mod
            ans = pow(d, n, mod)*combi.powe(y+n-1) * combi.rev_powe(y)*y
            print(ans % mod)
            return
        else:
            ans = 0
            print(ans % mod)
            return


def main():
    Q = int(input())
    for i in range(Q):
        solve()


if __name__ == "__main__":
    main()
