class Factorial:
    def __init__(self, max_fact, mod):
        #mod should be prime number
        #using homogeneous_product(n,r), max_fact ≧ max(n+r-1)
        f = [1] * (max_fact + 1)
        for idx in range(2, max_fact + 1):
            f[idx] = f[idx - 1] * idx
            f[idx] %= mod
        if mod > max_fact:
            fi = [pow(f[-1], mod - 2, mod)]
            for idx in range(max_fact, 0, -1):
                fi += [fi[-1] * idx % mod]
            fi = fi[::-1]
        else:
            fi = [pow(n, mod - 2, mod) for n in f]
        self.mod = mod
        self.f = f
        self.fi = fi

    def factorial(self, n):
        return self.f[n]

    def factorial_inverse(self, n):
        return self.fi[n]

    def combination(self, n, r):
        f = self.f
        fi = self.fi
        return f[n] * fi[r] * fi[n - r] % self.mod

    def permutation(self, n, r):
        return self.f[n] * self.fi[n - r] % self.mod

    def homogeneous_product(self, n, r):
        f = self.f
        fi = self.fi
        return f[n + r - 1] * fi[r] * fi[n - 1] % self.mod


max_fact = 2 * 10 ** 6
mod = 10**9 + 7
fact_instance = Factorial(max_fact, mod)
comb = fact_instance.combination
perm = fact_instance.permutation
combrep = fact_instance.homogeneous_product

H, W, A, B = [int(_) for _ in input().split()]
ans = comb(H + W - 2, H - 1)
for x in range(H - A, H):
    ans -= comb(x + B - 1, B - 1) * comb(H - 2 - x + W - B, W - B - 1)
    ans %= mod
print(ans)
