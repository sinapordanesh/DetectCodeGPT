import math
import numpy as np
import decimal
import collections
import itertools
import sys
import random
#Union-Find
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1 for i in range(self.n)]
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def unite(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q:
            return None
        if p > q:
            p, q = q, p
        self.par[p] += self.par[q]
        self.par[q] = p
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def size(self, x):
        return -self.par[self.find(x)]

#素数関連
def prime_numbers(x):
    if x < 2:
        return []
    prime_numbers = [i for i in range(x)]
    prime_numbers[1] = 0
    for prime_number in prime_numbers:
        if prime_number > math.sqrt(x):
            break
        if prime_number == 0:
            continue
        for composite_number in range(2 * prime_number, x, prime_number):
            prime_numbers[composite_number] = 0
    return [prime_number for prime_number in prime_numbers if prime_number != 0]
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    prime_number = 7
    difference = 4
    while prime_number <= math.sqrt(x):
        if x % prime_number == 0:
            return False
        prime_number += difference
        difference = 6 - difference
    return True
#Prime-Factorize
def prime_factorize(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    f = 3
    while f ** 2 <= n:
        if n % f == 0:
            res.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        res.append(n)
    return res
#nCr
mod = 10 ** 9 + 7
class nCr():
    def __init__(self, n):
        self.n = n
        self.fa = [1] * (self.n + 1)
        self.fi = [1] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.fa[i] = self.fa[i - 1] * i % mod
            self.fi[i] = pow(self.fa[i], mod - 2, mod)
    def comb(self, n, r):
        if n < r:return 0
        if n < 0 or r < 0:return 0
        return self.fa[n] * self.fi[r] % mod * self.fi[n - r] % mod
#拡張Euclidの互除法
def extgcd(a, b, d = 0):
    g = a
    if b == 0:
        x, y = 1, 0
    else:
        x, y, g = extgcd(b, a % b)
        x, y = y, x - a // b * y
    return x, y, g
#BIT
class BinaryIndexedTree():
    def __init__(self, n):
        self.n = n
        self.BIT = [0] * (self.n + 1)
    def add(self, i, x):
        while i <= self.n:
            self.BIT[i] += x
            i += i & -i
    def query(self, i):
        res = 0
        while i > 0:
            res += self.BIT[i]
            i -= i & -i
        return res
#Associative Array
class AssociativeArray():
    def __init__(self, q):
        self.dic = dict()
        self.q = q
    def solve(self):
        for i in range(self.q):
            Query = list(map(int, input().split()))
            if Query[0] == 0:
                x, y, z = Query
                self.dic[y] = z
            else:
                x, y = Query
                if y in self.dic:
                    print(self.dic[y])
                else:
                    print(0)
#Floor Sum
def floor_sum(n, m, a, b):
    res = 0
    if a >= m:
        res += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        res += n * (b // m)
        b %= m
    y_max = (a * n + b) // m
    x_max = y_max * m - b
    if y_max == 0:
        return res
    res += y_max * (n + (-x_max // a))
    res += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return res
#Z-Algorithm
def z_algorithm(s):
    str_len = len(s)
    res = [0] * str_len
    res[str_len - 1] = str_len
    i, j = 1, 0
    while i < str_len:
        while i + j < str_len and s[i + j] == s[j]:
            j += 1
        res[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < str_len and j > res[k] + k:
            res[i + k] = res[k]
            k += 1
        i += k
        j -= k
    return res
class Manacher():
    def __init__(self, s):
        self.s = s
    def coustruct(self):
        i, j = 0, 0 
        s_len = len(self.s)
        res = [0] * s_len
        while i < s_len:
            while i - j >= 0 and i + j < s_len and self.s[i - j] == self.s[i + j]:
                j += 1
            res[i] = j
            k = 1
            while i - k >= 0 and k + res[i - k] < j:
                k += 1
            i += k
            j -= k
#mod-sqrt
def mod_sqrt(a, p):
    if a == 0:
        return 0
    if p == 2:
        return 1
    k = (p - 1) // 2
    if pow(a, k, p) != 1:
        return -1
    while True:
        n = random.randint(2, p - 1)
        r = (n ** 2 - a) % p
        if r == 0:
            return n
        if pow(r, k, p) == p - 1:
            break
    k += 1
    w, x, y, z = n, 1, 1, 0
    while k:
        if k % 2:
            y, z = w * y + r * x * z, x * y + w * z
        w, x = w * w + r * x * x, 2 * w * x
        w %= p
        x %= p
        y %= p
        z %= p
        k >>= 1
    return y
n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
s_t = sum(t)
ans = [0]
for i in range(n):
    ans[-1] = min(ans[-1], v[i])
    for j in range(t[i] * 2):
        ans.append(v[i])
ans.pop()
ans.append(0)
for i in range(1, s_t * 2 + 1):
    ans[i] = min(ans[i - 1] + 1 / 2, ans[i])
for i in range(1, s_t * 2 + 1)[::-1]:
    ans[i - 1] = min(ans[i] + 1 / 2, ans[i - 1])
print(sum(ans) / 2)