# https://kmjp.hatenablog.jp/entry/2020/05/10/0900
# 数学的な問題


mod = 998244353

class COM:
    def __init__(self, n, MOD):
        self.n = n
        self.MOD = MOD
        self.fac = [0] * (n+1)
        self.finv = [0] * (n+1)
        self.inv = [0] * (n+1)
        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, n+1):
            self.fac[i] = self.fac[i-1] * i % MOD
            self.inv[i] = MOD - self.inv[MOD % i] * (MOD // i) % MOD
            self.finv[i] = self.finv[i-1] * self.inv[i] % MOD

    def calc(self, k):
        if k < 0:
            return 0
        return self.fac[self.n] * (self.finv[k] * self.finv[self.n-k] % self.MOD) % self.MOD

def main():
    N, M, K = map(int,input().split())

    # 隣り合う組がK以下のパターンを総当たりして解く
    if N > 1:
        cmbclass = COM(N-1, mod)
        cmb = cmbclass.calc
    else:
        cmb = lambda x:1
    res = 0
    for i in range(K+1):
        res += M * cmb(i) % mod * pow(M-1, N-i-1, mod)


    print(res % mod) 


if __name__ == "__main__":
    main()
